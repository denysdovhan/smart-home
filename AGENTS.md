# Smart Home Agent Instructions

This is a Docker-based smart home infrastructure using a stack-oriented architecture where services are organized into logical groups with Docker Compose files.

## Architecture Overview

- **Stack-based organization**: Each directory (`apps/`, `media/`, `network/`, `support/`, etc.) represents a service stack with its own `compose.yml`.
- **Shared environment**: `common.env` provides global settings (TZ, domains, SMTP) inherited by all stacks via the `smart-home` command.
- **Per-stack configuration**: Each stack has its own `.env` file for stack-specific secrets and overrides.
- **Unified management**: The `bin/smart-home` script provides centralized control over all stacks.

## System Overview

This is an Ubuntu system running as an LXC container on a Proxmox machine.
The host is a Beelink S12 Pro with 16GB RAM and 500GB storage.

## Key Patterns

### Environment Configuration

- `common.env.example` is the non-secret template for reference; actual `common.env` contains secret shared config and must never be committed to git.
- Stack-specific `.env` files contain secrets and must never be committed to git.
- Docker Compose uses: `--env-file .env --env-file $SMART_HOME_DIR/common.env`.

### Critical Variables

- `${DOCKER}` - data directory
- `${STORAGE}` - host mounts
- `${PUBLIC_DOMAIN}` - domain for services publicly available over the internet
- `${PRIVATE_DOMAIN}` - domain for services only accessible within the local network

### Service Dependencies

- **Network services**: Nginx Proxy Manager (ports 80/443) routes to internal services.
- **Authentication**: Pocket ID provides OIDC for services like Mealie, Paperless, and Wallos.
- **Monitoring**: Watchtower auto-updates containers, and Uptime Kuma monitors services.

### Volume Patterns

- `${DOCKER}/service-name:/container/config` for persistent app data.
- `${STORAGE}/media:/media` for shared media files using Servarr conventions.
- `/var/run/docker.sock` mounted for container management tools.

### Storage Layout

```text
.
├── dump
└── media
    ├── data
    │   ├── movies
    │   └── tv
    ├── downloads
    │   ├── movies
    │   └── tv
    └── paperless
        ├── documents
        └── media.lock
```

## CLI Workflow

The `smart-home` script is central to all operations:

```bash
# Manage all stacks
smart-home up                    # Start all services
smart-home update                # Pull, build, and restart all
smart-home down                  # Stop all stacks

# Manage a specific stack
smart-home media up              # Start only media stack
smart-home support restart       # Restart support services

# Manage a specific container in a specific stack
smart-home nvr up frigate
smart-home media down plex
```

Use the `smart-home` utility instead of direct `docker` or `docker compose` commands for running, starting, restarting, stopping, or otherwise managing services.

Only `smart-home` handles environment file loading and stack context properly.

## Service Integration Points

### Reverse Proxy (Nginx Proxy Manager)

- Exposes services on `${PUBLIC_DOMAIN}` subdomains.
- SSL certificates are managed through Let's Encrypt.
- Web UI runs on port 8081.

### Media Pipeline

- Overseerr: Request interface to Radarr/Sonarr.
- Prowlarr: Indexer management for all Arr apps.
- Transmission: Download client with organized paths (`/media/downloads`).
- File structure follows the [Servarr guide](https://wiki.servarr.com/docker-guide#consistent-and-well-planned-paths).

### Authentication And Security

- Pocket ID: OIDC provider for SSO across services.
- Pi-hole: DNS-level ad blocking (ports 53, 5300).
- Wireguard: VPN access (ports 51820/51821).

## Documentation System

- MkDocs with Material theme builds from the `docs/` directory.
- `smart-home docs` serves the local development site.
- GitHub Pages deployment runs through the `docs.yml` workflow.
- Hardware and software sections document physical and logical architecture.

## Common Maintenance Tasks

- **Add new stack**: Create `new-stack/compose.yml`, add environment variables, and update docs.
- **Update secrets**: Edit the stack's `.env` file and restart affected services.
- **Scale resources**: Modify `deploy.resources.limits` in compose files.
- **Backup strategy**: Use Backrest service (port 9898) for automated backups to external storage.

When working with this codebase, always consider stack boundaries and the shared environment impact of changes.

## Specific Service Limitations

- When editing Frigate `config.yaml` configuration, never edit it directly. Instead, suggest changes because they should be applied through the web UI.
