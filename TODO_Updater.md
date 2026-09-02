# JarbinLocalAPI — Project Synchronization & Distribution TODO

> A cross-platform system for distributing and synchronizing Jarbin projects between Linux, Windows, and Android devices through JarbinLocalAPI.

---

# 1. Define the System Architecture

- [ ] Define the synchronization subsystem independently from the existing package/cache service.
- [ ] Decide whether the synchronization system lives inside JarbinLocalAPI or in a dedicated Python program.
- [ ] Define the concepts of:
  - [ ] Projects
  - [ ] Devices
  - [ ] Snapshots
  - [ ] File manifests
  - [ ] File objects
  - [ ] Updates
  - [ ] Conflicts
- [ ] Define the server as the source of truth for synchronized projects.
- [ ] Keep the implementation cross-platform:
  - [ ] Linux
  - [ ] Windows
  - [ ] Android / Termux

Suggested structure:

```text
JarbinLocalAPI
└── Sync
    ├── Projects
    ├── Devices
    ├── Snapshots
    ├── Objects
    └── Updates
```

---

# 2. Project Repository

- [ ] Implement server-side project storage.
- [ ] Give every synchronized project a unique identifier.
- [ ] Store the current project state on the server.
- [ ] Store historical project snapshots.
- [ ] Keep the latest snapshot identifiable as the current version.

Example:

```text
projects/
└── JarEngine/
    ├── snapshots/
    │   ├── a82f31
    │   ├── c91842
    │   └── d72a11
    └── ...
```

---

# 3. File Hashing

- [ ] Hash every tracked file.
- [ ] Use a strong content hash such as SHA-256.
- [ ] Store the hash together with the relative file path.
- [ ] Detect modifications by comparing hashes rather than timestamps.
- [ ] Detect newly created files.
- [ ] Detect deleted files.

Example manifest:

```json
{
    "src/main.py": "abc123...",
    "src/player.py": "91f821...",
    "assets/player.png": "42a991..."
}
```

---

# 4. Snapshots

- [ ] Create immutable snapshots of project states.
- [ ] Give every snapshot a unique identifier.
- [ ] Associate each snapshot with its file manifest.
- [ ] Store creation time.
- [ ] Store the device that created the snapshot.
- [ ] Optionally store a human-readable description/message.

Example:

```text
JarEngine

a82f31
    Initial synchronization

c91842
    Multiplayer changes

d72a11
    Network fixes
```

---

# 5. Content-Addressed File Storage

- [ ] Store files using their content hash.
- [ ] Avoid storing the same file multiple times.
- [ ] Allow multiple snapshots to reference the same file object.
- [ ] Separate file objects from project snapshots.

Conceptually:

```text
objects/
├── ab/
│   └── c123...
├── 91/
│   └── f821...
└── 42/
    └── a991...
```

A snapshot then references those objects:

```text
JarEngine / snapshot c91842

src/main.py       → abc123
src/player.py     → 91f821
assets/player.png → 42a991
```

---

# 6. Client Registration

- [ ] Give each device a unique identifier.
- [ ] Store device name.
- [ ] Store operating system.
- [ ] Store architecture where relevant.
- [ ] Track the last connection.
- [ ] Track the projects installed/synchronized on the device.

Example:

```json
{
    "id": "device_01",
    "name": "Jarjarbin-PC",
    "platform": "linux",
    "architecture": "x86_64"
}
```

Possible devices:

```text
Jarjarbin-PC       Linux
Jarjarbin-Laptop   Windows
Jarjarbin-Phone    Android
```

---

# 7. Client Manifest

- [ ] Create a client-side manifest for each synchronized project.
- [ ] Record the currently installed snapshot.
- [ ] Record tracked file hashes.
- [ ] Detect local changes before synchronization.
- [ ] Detect files added locally.
- [ ] Detect files deleted locally.

Example:

```json
{
    "project": "JarEngine",
    "snapshot": "a82f31",
    "files": {
        "src/main.py": "abc123",
        "src/player.py": "91ffff",
        "Makefile": "11ad72"
    }
}
```

---

# 8. Synchronization Status

Implement a status operation before implementing automatic updates.

- [ ] Add a project status endpoint.
- [ ] Compare the client's snapshot against the server snapshot.
- [ ] Identify files that are:
  - [ ] Unchanged
  - [ ] Added on the server
  - [ ] Modified on the server
  - [ ] Deleted on the server
  - [ ] Added locally
  - [ ] Modified locally
  - [ ] Deleted locally
  - [ ] Conflicting
- [ ] Return a machine-readable status.

Example:

```http
POST /sync/JarEngine/status
```

Response:

```json
{
    "server_snapshot": "c91842",
    "client_snapshot": "a82f31",
    "changes": [
        {
            "path": "src/network.py",
            "action": "add"
        },
        {
            "path": "src/player.py",
            "action": "update"
        }
    ]
}
```

---

# 9. Pull / Update

- [ ] Implement downloading server changes.
- [ ] Only transfer files that are actually required.
- [ ] Transfer deletion instructions for removed files.
- [ ] Update the local manifest after a successful update.
- [ ] Update the local snapshot identifier.
- [ ] Make the operation atomic where possible.
- [ ] Prevent a failed transfer from leaving the project in a partially updated state.

Suggested endpoint:

```http
POST /sync/{project}/pull
```

Or a convenience endpoint:

```http
POST /update
```

Example response:

```json
{
    "from": "a82f31",
    "to": "c91842",
    "files": [
        "src/network.py",
        "src/player.py"
    ]
}
```

---

# 10. Push

- [ ] Implement uploading local changes to the server.
- [ ] Send the client's base snapshot.
- [ ] Send only files that changed locally.
- [ ] Upload new files.
- [ ] Upload modified files.
- [ ] Report deleted files.
- [ ] Create a new server snapshot after successful validation.

Suggested endpoint:

```http
POST /sync/{project}/push
```

The server should know:

```text
Client base:
    a82f31

Client changes:
    + src/network.py
    ~ src/player.py
    - src/old_system.py
```

---

# 11. Conflict Detection

This is a critical part of the system.

- [ ] Detect when the server changed a file after the client's base snapshot.
- [ ] Detect when the client also changed that same file.
- [ ] Do not silently overwrite either version.
- [ ] Return explicit conflict information.
- [ ] Preserve the conflicting files.
- [ ] Provide enough information for a client to resolve the conflict.

Example:

```json
{
    "status": "conflict",
    "files": [
        {
            "path": "src/player.py",
            "reason": "modified_on_both_sides"
        }
    ]
}
```

Possible future resolution strategies:

```text
Keep local
Keep server
Manual merge
Create separate snapshot
```

---

# 12. Incremental Updates

- [ ] Ensure normal updates do not require downloading the entire project.
- [ ] Calculate differences between snapshots.
- [ ] Transfer only required file objects.
- [ ] Transfer deletion instructions separately.
- [ ] Reuse already-existing content-addressed files.

Example:

```text
Project size:       2.4 GB
Changed files:      14 MB

Full update:        2.4 GB
Incremental update: 14 MB
```

---

# 13. Compression

- [ ] Compress update transfers.
- [ ] Start with a simple and widely supported archive format such as ZIP.
- [ ] Group multiple changed files into one update archive when beneficial.
- [ ] Avoid unnecessary compression of already-compressed formats.
- [ ] Preserve file paths and metadata required by the client.
- [ ] Consider Zstandard later if performance becomes important.

Example:

```text
Server changes
      │
      ▼
update.zip
      │
      ▼
Client
      │
      ▼
Extract changed files
```

---

# 14. Full Project Download

Incremental synchronization should be the default, but full downloads should remain possible.

- [ ] Implement a full project download.
- [ ] Generate a compressed project archive.
- [ ] Include the current snapshot identifier.
- [ ] Include the complete project structure.
- [ ] Allow a new device to initialize directly from the server.

Example:

```http
GET /sync/JarEngine/archive
```

This is particularly useful for:

```text
New device
    ↓
Download complete project
    ↓
Create local manifest
    ↓
Start incremental synchronization
```

---

# 15. `/update` Convenience Operation

- [ ] Create a high-level `/update` endpoint.
- [ ] Allow a client to request updates for selected projects.
- [ ] Identify the client's current snapshot.
- [ ] Return only the necessary changes.
- [ ] Allow the client to automatically apply them.

Example:

```http
POST /update
```

```json
{
    "device": "Jarjarbin-Laptop",
    "projects": [
        "JarEngine",
        "Jarbin-ToolKit",
        "JarTest"
    ]
}
```

Response:

```json
{
    "updates": [
        {
            "project": "JarEngine",
            "updated": true,
            "snapshot": "c91842"
        },
        {
            "project": "Jarbin-ToolKit",
            "updated": false
        },
        {
            "project": "JarTest",
            "updated": true,
            "snapshot": "82a991"
        }
    ]
}
```

---

# 16. Automatic Update Checks

- [ ] Allow a device to request synchronization when it connects.
- [ ] Allow clients to periodically check for updates.
- [ ] Allow the server to expose whether an update is available.
- [ ] Allow per-device project subscriptions.
- [ ] Avoid automatically modifying a project without client-side confirmation unless explicitly configured.

Example:

```text
Device connects
      │
      ▼
GET /sync/status
      │
      ▼
Update available?
   ┌──┴──┐
   │     │
  No    Yes
   │     │
   │     ▼
   │   Pull update
   │
Done
```

---

# 17. Cross-Platform Client

- [ ] Create a Python client for the synchronization protocol.
- [ ] Make the client work on Linux.
- [ ] Make the client work on Windows.
- [ ] Make the client work on Android through Termux.
- [ ] Avoid platform-specific behavior in the core synchronization logic.
- [ ] Isolate platform-specific filesystem operations.

Possible command interface:

```bash
jarbin sync status JarEngine
jarbin sync pull JarEngine
jarbin sync push JarEngine
jarbin sync update JarEngine
jarbin sync history JarEngine
```

---

# 18. Project History

- [ ] Provide access to historical snapshots.
- [ ] List snapshots for a project.
- [ ] Inspect the files belonging to a snapshot.
- [ ] Compare two snapshots.
- [ ] Allow downloading a historical snapshot.
- [ ] Consider restoring a project to a previous snapshot.

Example:

```http
GET /sync/JarEngine/history
GET /sync/JarEngine/snapshots/c91842
GET /sync/JarEngine/diff/a82f31/c91842
```

---

# 19. Device / Project Permissions

- [ ] Decide which devices can access synchronization.
- [ ] Allow project-specific permissions.
- [ ] Allow read-only devices.
- [ ] Allow read/write devices.
- [ ] Prevent unauthorized devices from modifying projects.

Example:

```text
Jarjarbin-PC
    JarEngine       READ / WRITE

Jarjarbin-Laptop
    JarEngine       READ / WRITE
    JarTest         READ ONLY

Jarjarbin-Phone
    JarEngine       READ ONLY
```

---

# 20. Integrity Verification

- [ ] Verify downloaded file hashes.
- [ ] Verify the resulting project manifest after synchronization.
- [ ] Reject corrupted or incomplete objects.
- [ ] Verify the final snapshot before marking synchronization as successful.
- [ ] Make synchronization failures recoverable.

Example:

```text
Download
   ↓
SHA-256 verification
   ↓
Write file
   ↓
Recalculate manifest
   ↓
Compare with snapshot
   ↓
Mark synchronized
```

---

# 21. API Design

Suggested API structure:

```text
/sync
├── /projects
│   ├── GET
│   └── ...
│
├── /devices
│   ├── POST /register
│   ├── GET
│   └── ...
│
├── /{project}
│   ├── /status
│   ├── /push
│   ├── /pull
│   ├── /history
│   ├── /snapshots
│   └── /archive
│
└── /objects
    └── /{hash}
```

Convenience endpoint:

```text
/update
```

---

# 22. Server Storage Model

Design storage so that project metadata and file objects are separated.

Possible structure:

```text
data/
└── sync/
    ├── projects/
    │   └── JarEngine/
    │       ├── metadata.json
    │       └── snapshots/
    │           ├── a82f31.json
    │           └── c91842.json
    │
    ├── objects/
    │   ├── ab/
    │   ├── 91/
    │   └── 42/
    │
    └── devices/
        ├── device_01.json
        └── device_02.json
```

The exact storage format can be changed later.

---

# 23. Dashboard Integration

The synchronization system should eventually integrate with the JarbinLocalAPI dashboard.

Example:

```text
PROJECTS

JarEngine
    Server: c91842
    PC:     c91842       ✓
    Laptop: a82f31       UPDATE AVAILABLE
    Phone:  c91842       ✓
```

Possible actions:

```text
[ View History ]
[ View Changes ]
[ Create Snapshot ]
[ Download Archive ]
```

---

# 24. Initial MVP

The first implementation should remain small.

### MVP server

- [ ] One project
- [ ] File hashing
- [ ] Server-side manifest
- [ ] Snapshots
- [ ] Device registration
- [ ] Status endpoint
- [ ] Full pull
- [ ] Incremental pull
- [ ] Basic push
- [ ] Basic conflict detection
- [ ] ZIP-compressed transfers

### MVP client

- [ ] Python client
- [ ] Linux support
- [ ] Windows support
- [ ] Android / Termux support
- [ ] Local manifest
- [ ] `status`
- [ ] `pull`
- [ ] `push`
- [ ] `update`

---

# Final Goal

The finished system should allow the same project to exist on multiple devices while keeping them synchronized through JarbinLocalAPI:

```text
                         JarbinLocalAPI
                               │
                       Project Repository
                               │
                    ┌──────────┼──────────┐
                    │          │          │
                  Linux      Windows    Android
                    │          │          │
                 JarEngine  JarEngine  JarEngine
                    │          │          │
                    └──────────┬──────────┘
                               │
                         Synchronization
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
              Snapshots      Hashes        Deltas
                 │             │             │
                 └─────────────┼─────────────┘
                               │
                         Conflict detection
```

The core principle is:

> **Do not replace an entire project unless necessary. Identify the exact project state, calculate the difference, transfer only the required content, and refuse to silently overwrite conflicting changes.**

This makes JarbinLocalAPI a personal, cross-platform project distribution and synchronization system rather than merely a file download server.
