# Authentication Lab Runbook

Use only these two projects:

- `dishonored_api`
- `dishonored_git`

Do not use `dishonoured_backend`.

## Server Machine

1. Find the server LAN IP:
   `ipconfig`

2. Start the API over HTTPS:
   `dotnet run --launch-profile https`

3. The API listens on:
   `https://<server-lan-ip>:7018`

## Client Machine

1. In `dishonored_git`, create `.env` from `.env.example`.

2. Set the API URL to the server machine:
   `VITE_API_BASE_URL=https://<server-lan-ip>:7018`

3. Start the React app over HTTPS:
   `npm run dev:https`

4. Open the client URL shown by Vite, for example:
   `https://<client-lan-ip>:5173`

The browser may ask you to trust the local development certificate. Accept it for the lab network demo.

## Demo Checklist

- Register creates a `USER` account.
- Login returns a signed token.
- Profile is protected and redirects to login without a token.
- Character edits require the authenticated `USER` token.
- Logout revokes the server-side session.
- Inactivity logs the user out after 15 minutes.
