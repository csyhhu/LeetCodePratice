# Secure Backup Recovery Guide

This guide explains how to decrypt and restore the encrypted interview backups.

## Prerequisites

- Encrypted files (`*.enc`) under `.secure_backups/`
- The matching key file (`backup.key`)
- `openssl` and `tar` available on macOS

Important:
- Do NOT upload `backup.key` to GitHub.
- Keep encrypted files and key in separate storage locations.

## 1) Go to project directory

```bash
cd "/Users/chenshangyu/WorkSpace/LeetCodePratice"
```

## 2) Check encrypted backup files

```bash
ls -lh .secure_backups/*.enc
```

Expected examples:
- `.secure_backups/AI-Native-Coding_20260430_183450.tar.gz.enc`
- `.secure_backups/behavior_20260430_183451.tar.gz.enc`

## 3) Restore into a temporary directory (recommended)

```bash
cd "/Users/chenshangyu/WorkSpace/LeetCodePratice"
RESTORE_DIR="$HOME/Desktop/meta_restore_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$RESTORE_DIR"

# Decrypt + extract AI-Native Coding
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 \
  -in ".secure_backups/AI-Native-Coding_20260430_183450.tar.gz.enc" \
  -out "$RESTORE_DIR/AI-Native-Coding.tar.gz" \
  -pass file:.secure_backups/backup.key
tar -xzf "$RESTORE_DIR/AI-Native-Coding.tar.gz" -C "$RESTORE_DIR"

# Decrypt + extract behavior
openssl enc -d -aes-256-cbc -pbkdf2 -iter 200000 \
  -in ".secure_backups/behavior_20260430_183451.tar.gz.enc" \
  -out "$RESTORE_DIR/behavior.tar.gz" \
  -pass file:.secure_backups/backup.key
tar -xzf "$RESTORE_DIR/behavior.tar.gz" -C "$RESTORE_DIR"

# Verify restored content
ls -lah "$RESTORE_DIR"
```

## 4) Copy restored data back to repo (optional)

Only run this if you want to overwrite/update current local folders.

```bash
rsync -a "$RESTORE_DIR/AI-Native Coding/" "/Users/chenshangyu/WorkSpace/LeetCodePratice/AI-Native Coding/"
rsync -a "$RESTORE_DIR/behavior/" "/Users/chenshangyu/WorkSpace/LeetCodePratice/behavior/"
```

## 5) Clean temporary plaintext files

```bash
rm -f "$RESTORE_DIR/AI-Native-Coding.tar.gz" "$RESTORE_DIR/behavior.tar.gz"
```

If everything is confirmed, remove full temp directory:

```bash
rm -rf "$RESTORE_DIR"
```

## Common errors

- `bad decrypt` / `invalid password`
  - Usually wrong key or mismatched `backup.key`.

- `tar: Error opening archive`
  - Decryption likely failed, resulting tar file is invalid.

- Key file moved elsewhere
  - Replace `-pass file:.secure_backups/backup.key` with actual path:

```bash
-pass file:/absolute/path/to/backup.key
```

## What to upload

Safe to upload:
- `.secure_backups/*.enc`
- This guide file

Do NOT upload:
- `.secure_backups/backup.key`
- Any decrypted `*.tar.gz` or extracted plaintext folders
