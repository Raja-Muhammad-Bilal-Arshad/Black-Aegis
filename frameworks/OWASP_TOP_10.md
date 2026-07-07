# OWASP Top 10 (2025 Standard)

> Standard for Web Application Security.
> **Directive**: "Test for these in every web engagement."

## A01: Broken Access Control
> Users acting outside of their intended permissions.
- [ ] **IDOR**: Changing `id=100` to `id=101` in URL/POST body.
- [ ] **Forced Browsing**: Accessing `/admin` as an unauthenticated user.
- [ ] **Method Manipulation**: Changing `GET` to `POST` (or `PUT`/`DELETE`).

## A02: Cryptographic Failures
> Exposure of sensitive data due to weak crypto.
- [ ] **Weak Ciphers**: SSL Labs scan (Grade C or lower?).
- [ ] **Cleartext Data**: Searching for `password`, `key`, `token` in HTTP traffic.
- [ ] **Default Keys**: Testing common default JWT secrets (e.g., "secret").

## A03: Injection
> Untrusted data sent to an interpreter as part of a command.
- [ ] **SQLi**: Input `' OR 1=1 --` in login forms and ID parameters.
- [ ] **Command Injection**: Input `; id` or `| whoami` in fields that might trigger shell scripts.
- [ ] **LDAP Injection**: Input `*` or `)(cn=*` in login fields.

## A04: Insecure Design
> Flaws in the architecture itself (missing controls).
- [ ] **Business Logic**: Can you buy an item for $0.00?
- [ ] **Rate Limiting**: Can you brute force the login 10,000 times without lock?

## A05: Security Misconfiguration
> Default configs, verbose errors, open storage.
- [ ] **Verbose Errors**: Do stack traces leak paths/versions?
- [ ] **Default Creds**: `admin:admin`, `tomcat:s3cret`.
- [ ] **Open Buckets**: S3/Azure blobs accessible without auth.

## A06: Vulnerable and Outdated Components
> Using libraries with known CVEs.
- [ ] **Version Detection**: Check `jQuery`, `Bootstrap`, `React` versions.
- [ ] **CVE Scan**: Run `retire.js` or `dependency-check`.

## A07: Identification and Authentication Failures
> Weak login forms, session management issues.
- [ ] **Credential Stuffing**: Does the app allow automated login attempts?
- [ ] **Weak Policies**: Does it allow "password123"?
- [ ] **Session Fixation**: Does the session ID change after login?

## A08: Software and Data Integrity Failures
> Code/CI-CD pipeline insecurity, deserialization.
- [ ] **Deserialization**: Look for base64 blobs (Java/Python objects).
- [ ] **CI/CD Poisoning**: Can you access the Jenkins/Gitlab instance?

## A09: Security Logging and Monitoring Failures
> Lack of alerts for active attacks.
- [ ] **Trigger Events**: Generate 404s/500s. Does the SOC notice?
- [ ] **Log Injection**: Inject `\n [INFO] User Admin Logged In` into User-Agent.

## A10: Server-Side Request Forgery (SSRF)
> Fetching a remote resource from the server.
- [ ] **Metadata Access**: Input `http://169.254.169.254/` in URL parameters.
- [ ] **Internal Port Scan**: Input `http://localhost:22`.
