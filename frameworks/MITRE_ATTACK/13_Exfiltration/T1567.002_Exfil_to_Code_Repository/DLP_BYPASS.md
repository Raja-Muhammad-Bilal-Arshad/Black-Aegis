# DLP Bypass Guide: Code Repositories (T1567.002)

## Developer Exceptions
Developers often have unrestricted access to GitHub/GitLab/Bitbucket. Activity here is expected to be high-volume uplinks.

## Evasion Techniques
1.  **Private Repos**: Pushing to a private repository means the Blue Team cannot see what was uploaded even if they see the URL in logs.
2.  **Steganography in Commits**: Hiding data in commit messages or inside innocuous-looking binary assets (images in the repo).
