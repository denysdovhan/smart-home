# Smart Home Copilot Instructions

This is a Docker-based smart home infrastructure using a stack-oriented architecture where services are organized into logical groups with Docker compose files.

## Architecture Overview

- **Stack-based organization**: Each directory (`apps/`, `media/`, `network/`, `support/`, etc.) represents a service stack with its own `compose.yml`.
- **Shared environment**: `common.env` provides global settings (TZ, domains, SMTP) inherited by all stacks via `smart-home` command.
- **Per-stack configuration**: Each stack has its own `.env` file for stack-specific secrets and overrides.
- **Unified management**: The `bin/smart-home` script provides centralized control over all stacks.

## Key Development Patterns

### Environment Configuration

- `common.env.example` is the non-secret template for reference; actual `common.env` contains secret shared config (never commited to git).
- Stack-specific `.env` files contain secrets (never committed to git).
- Docker compose uses: `--env-file .env --env-file $SMART_HOME_DIR/common.env`.

### Critical variables

- `${DOCKER}` - data directory
- `${STORAGE}` - host mounts
- `${PUBLIC_DOMAIN}` - domain for services publicly available over the internet
- `${PRIVATE_DOMAIN}` - domain for services only accessible within the local network

### Service Dependencies

- **Network services**: Nginx Proxy Manager (ports 80/443) routes to internal services
- **Authentication**: Pocket ID provides OIDC for services like Mealie, Paperless, Wallos
- **Monitoring**: Watchtower auto-updates containers, Uptime Kuma monitors services

### Volume Patterns

- `${DOCKER}/service-name:/container/config` for persistent app data
- `${STORAGE}/media:/media` for shared media files (using Servarr conventions)
- `/var/run/docker.sock` mounted for container management tools

### Storage layout

```
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
smart-home update               # Pull, build, and restart all
smart-home down                 # Stop all stacks

# Manage specific stack
smart-home media up             # Start only media stack
smart-home support restart      # Restart support services
```

Always use the script rather than direct `docker compose` commands—it handles environment file loading and stack context.

## Service Integration Points

### Reverse Proxy (Nginx Proxy Manager)

- Exposes services on `${PUBLIC_DOMAIN}` subdomains
- SSL certificates via Let's Encrypt
- Web UI on port 8081

### Media Pipeline

- Overseerr: Request interface → Radarr/Sonarr
- Prowlarr: Indexer management for all Arr apps
- Transmission: Download client with organized paths (`/media/downloads`)
- File structure follows [Servarr guide](https://wiki.servarr.com/docker-guide#consistent-and-well-planned-paths)

### Authentication & Security

- Pocket ID: OIDC provider for SSO across services
- Pi-hole: DNS-level ad blocking (ports 53, 5300)
- Wireguard: VPN access (ports 51820/51821)

## Documentation System

- MkDocs with Material theme builds from `docs/` directory
- `smart-home docs` serves local development site
- GitHub Pages deployment via docs.yml workflow
- Hardware and software sections document physical and logical architecture

## Common Maintenance Tasks

- **Add new stack**: Create `new-stack/compose.yml`, add environment variables, update docs
- **Update secrets**: Edit stack's `.env` file, restart affected services
- **Scale resources**: Modify `deploy.resources.limits` in compose files
- **Backup strategy**: Use Backrest service (port 9898) for automated backups to external storage

When working with this codebase, always consider the stack boundaries and shared environment impact of changes.
