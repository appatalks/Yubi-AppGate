# Yubi AppGate

Lock your Android apps behind a physical YubiKey using HMAC-SHA1 challenge-response authentication. No passwords to remember, no PINs to guess. If you don't have the key, you don't get in.

[Website](https://appatalks.github.io/Yubi-AppGate/) · [Get it on Google Play](https://play.google.com/store/apps/details?id=com.appatalks.yubi_appgate)

## What It Does

- Locks any app behind your YubiKey (NFC or USB-C)
- System-wide protection via accessibility service: blocks protected apps no matter how they're launched
- Optional uninstall protection through Device Administrator mode
- Entirely offline. No accounts, no cloud, no telemetry

## Getting Started

1. Install Yubi AppGate from Google Play
2. Plug in or tap your YubiKey to enroll it
3. Pick the apps you want to protect
4. (Optional) Enable system-wide protection in Settings → Accessibility → Yubi AppGate

For a full walkthrough, see the [How It Works](https://appatalks.github.io/Yubi-AppGate/how-it-works.html) page.

## Free vs Pro

| | Free | Pro ($6.99) |
|---|---|---|
| Protected apps | 2 | Unlimited |
| YubiKey enrollment | Yes | Yes |
| System-wide protection | Yes | Yes |
| Uninstall protection | Yes | Yes |
| License | — | Lifetime |

## Feedback and Issues

This repository doubles as the support portal for Yubi AppGate. If you have a bug report, feature request, or question:

- [Open an issue](https://github.com/appatalks/Yubi-AppGate/issues)

Please include your Android version and device model when reporting bugs.

## Security

Yubi AppGate never stores your YubiKey's secret. Each unlock generates a fresh HMAC-SHA1 challenge and verifies the response on-device. No data leaves your phone.

For details on the authentication architecture, see the [Security](https://appatalks.github.io/Yubi-AppGate/security.html) page.

## Privacy

The app collects no personal data. No analytics, no crash reporting, no network calls. Full policy: [Privacy Policy](https://appatalks.github.io/Yubi-AppGate/privacy.html).

## License

This website content is proprietary. The Yubi AppGate source code is maintained in a separate private repository.
