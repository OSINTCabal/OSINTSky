# Authentication Guide

## Why Authentication is Required

BlueSky's AT Protocol requires authentication for all API access, including public data searches. This is different from 4chan/8kun which have fully open APIs.

## How to Authenticate

### Option 1: Main Password (Quick Start)
```bash
python3 blueskyosint.py

# When prompted:
BlueSky Handle: your.handle.bsky.social
Password: your_main_password
```

### Option 2: App Password (Recommended for OPSEC)

**More secure - doesn't use your main password**

1. **Create App Password:**
   - Log into BlueSky web or app
   - Go to: Settings > Advanced > App passwords
   - Click "Add App Password"
   - Name it: "OSINTTool" or similar
   - Copy the generated password

2. **Use in BlueSkyOSINT:**
```bash
python3 blueskyosint.py

# When prompted:
BlueSky Handle: your.handle.bsky.social
Password: [paste your app password]
```

## Security Considerations

### Your Credentials
- **NOT stored anywhere** - only used for session creation
- **Session tokens expire** - credentials needed each run
- **Not logged or saved** - password never written to disk

### Best Practices
1. **Use app passwords** instead of main password
2. **Create dedicated account** for investigations
3. **Use Tor/VPN** when authenticating
4. **Rotate app passwords** regularly
5. **Delete app passwords** when done investigating

### Dedicated Investigation Account

**Recommended Setup:**
```
1. Create new BlueSky account: investigator.example.bsky.social
2. Use throwaway email
3. Generate app password
4. Use only with BlueSkyOSINT
5. Delete account when investigation complete
```

## Session Management

BlueSkyOSINT uses the atproto library which:
- Creates access tokens (expire after a few minutes)
- Creates refresh tokens (last longer)
- Automatically refreshes expired tokens
- Manages session state

**You don't need to worry about token management - it's automatic!**

## Authentication Errors

### "Invalid username or password"
- Check handle spelling (should be: user.bsky.social)
- Verify password is correct
- If using app password, ensure it's not expired

### "Network error"
- Check internet connection
- Try without proxy first
- Verify BlueSky isn't down

### "Rate limited"
- BlueSky limits authentication attempts
- Wait 5-10 minutes before retrying
- Consider if account is locked

## Multi-Account Usage

**For investigations requiring multiple accounts:**

```python
# Account 1 session
tool1 = BlueSkyOSINT()
tool1.login()  # Uses account1 credentials
tool1.search_posts("topic1")

# Account 2 session  
tool2 = BlueSkyOSINT()
tool2.login()  # Uses account2 credentials
tool2.search_posts("topic2")
```

## Troubleshooting

**"atproto library not installed"**
```bash
pip install atproto --break-system-packages
```

**"Authentication failed"**
- Verify credentials
- Check if 2FA is enabled (not supported)
- Try app password instead

**"Session expired"**
- Restart tool and re-authenticate
- This is normal after extended periods

## Privacy Notes

- BlueSky logs authentication from your IP
- Use VPN/Tor for anonymity
- Dedicated accounts recommended for sensitive work
- App passwords can be revoked any time
- Authentication is required by BlueSky, not this tool

---

**Remember**: Authentication is a BlueSky requirement, not a limitation of this tool. Once authenticated, you have full access to all public data on the platform.
