# OSINTSky

<div align="center">

**Professional OSINT Tool for BlueSky/AT Protocol**

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey.svg)](https://github.com/OSINTCabal/OSINTSky)

*Comprehensive intelligence gathering for BlueSky Social (AT Protocol)*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation)

</div>

---

## 🎯 Features

**21 Intelligence Gathering Functions**

### 🔍 Search & Discovery
- Keyword search across BlueSky
- Hashtag monitoring  
- Advanced search with filters
- Trending posts discovery
- User mention tracking

### 👤 User Intelligence
- Complete profile analysis
- Timeline collection & archiving
- Liked posts analysis
- Reply pattern tracking
- Activity & engagement statistics

### 🕸️ Network Analysis
- Follower/following lists
- **Network Mapper** - Compare 2 accounts, find shared connections
- **Community Detection** - Analyze account structure & social role

### 📡 Real-time Monitoring
- Single user tracking
- Hashtag trend monitoring
- Multi-user simultaneous tracking

### 🎨 Professional Interface
- Loading animations & progress bars
- Color-coded output
- Emoji icons for clarity
- Clean terminal UI

---

## 📋 Requirements

- Python 3.7+
- BlueSky account
- Internet connection

---

## 🚀 Installation

### Quick Install

```bash
git clone https://github.com/OSINTCabal/OSINTSky.git
cd OSINTSky
pip install -r requirements.txt
python3 blueskyosint.py
```

### Manual Install

```bash
pip install atproto colorama
python3 blueskyosint.py
```

---

## 🔐 Authentication

Login with your BlueSky credentials when prompted:

```
Handle: your.handle.bsky.social
Password: your_password
```

**Security Tips:**
- Credentials are NOT stored
- Session-only authentication
- Use [app passwords](https://bsky.app/settings/app-passwords) for security
- See [AUTHENTICATION.md](AUTHENTICATION.md) for details

---

## 📖 Usage

### Quick Start

```bash
python3 blueskyosint.py
```

### Example: Profile Investigation

```
1. Profile User (Option 6) → Get overview
2. Collect Timeline (Option 7) → Archive posts  
3. Activity Analysis (Option 10) → Statistics
4. Export Results (Option 18) → Save as JSON
```

### Example: Find Connections

```
Network Mapper (Option 13)
  Account 1: suspect1.bsky.social
  Account 2: suspect2.bsky.social
  Result: Shared followers & following
```

### Example: Real-time Monitoring

```
Monitor User (Option 15)
  Track: target.bsky.social
  Interval: 60 seconds
  Duration: 300 seconds
```

---

## 📚 Documentation

- **[AUTHENTICATION.md](AUTHENTICATION.md)** - Security & login guide
- **[NETWORK_ANALYSIS_GUIDE.md](NETWORK_ANALYSIS_GUIDE.md)** - Advanced network analysis
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute getting started guide
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines

---

## 🛡️ OPSEC

### Using with Tor

```bash
proxychains4 python3 blueskyosint.py
```

### Best Practices
- Use VPN/Tor for anonymity
- Create dedicated investigation account
- Use app passwords
- Export to encrypted storage
- Rotate credentials regularly

---

## ⚖️ Legal Notice

**For Legitimate Use Only**

✅ Licensed investigators  
✅ Law enforcement  
✅ Security researchers  
✅ Journalists  
✅ Academic research  

❌ Harassment  
❌ Unauthorized surveillance  
❌ Commercial scraping  
❌ ToS violations  

**You are responsible for legal compliance.**

---

## 🔧 Technical

### Dependencies
- `atproto` - AT Protocol SDK
- `colorama` - Terminal colors

### API Endpoints
- `app.bsky.feed.searchPosts`
- `app.bsky.actor.getProfile`
- `app.bsky.feed.getAuthorFeed`
- `app.bsky.graph.getFollowers`
- `app.bsky.graph.getFollows`

---

## 🐛 Troubleshooting

**Authentication Failed**
- Verify credentials
- Try app password
- Check 2FA is disabled

**Network Error**
- Check connection
- Try without proxy
- Verify BlueSky status

**No Results**
- Broaden search terms
- Check account privacy
- Verify handle spelling

---

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

- Report bugs
- Suggest features
- Improve docs
- Submit PRs

---

## 📊 Roadmap

- [ ] Advanced filtering
- [ ] Media downloads
- [ ] Graph visualization
- [ ] Sentiment analysis
- [ ] CSV export
- [ ] Historical comparison

---

## 👤 Author

**OSINTCabal**

- GitHub: [@OSINTCabal](https://github.com/OSINTCabal)
- BlueSky: [@osintcabal.bsky.social](https://bsky.app/profile/osintcabal.bsky.social)

---

## 🌟 Related Projects

- [ChanSINT](https://github.com/OSINTCabal/ChanSINT) - 4chan/8kun OSINT
- [TelegramOSINT-Kit](https://github.com/OSINTCabal/TelegramOSINT) - Telegram Intelligence
- [SneakLeak](https://github.com/OSINTCabal/SneakLeak) - Breach Data Analysis

---

## 📜 License

MIT License - See [LICENSE](LICENSE)

---

<div align="center">

**Built for the OSINT Community** 🔍

Professional intelligence gathering for BlueSky/AT Protocol

⭐ Star this repo if you find it useful!

</div>
