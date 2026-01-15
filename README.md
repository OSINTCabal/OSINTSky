# BlueSkyOSINT

<div align="center">

                    ```
              .=***********=.              
          .*********************.          
        ***************************        
      *******************************      
    =*********************************=    
   *************************************   
  ********** ***************** **********  
 **********     ***********     ********** 
.**********       *******       **********.
***********        -***-        ***********
***********          *          ***********
************                   ************
**************.             .**************
**************               +*************
.************        *        ************.
 *************.     ***     .************* 
  **************+ +*****+ +**************  
   *************************************   
    =*********************************=    
      *******************************      
        ***************************        
          .*********************.          
              .=***********=.              

  ___  ____ ___ _   _ _____ ____  _          
 / _ \/ ___|_ _| \ | |_   _/ ___|| | ___   _ 
| | | \___ \| ||  \| | | | \___ \| |/ / | | |
| |_| |___) | || |\  | | |  ___) |   <| |_| |
 \___/|____/___|_| \_| |_| |____/|_|\_\\__, |
                                       |___/ 
```

**BlueSky OSINT Intelligence Tool - AT Protocol Edition**   

A comprehensive OSINT tool for collecting and analyzing public data from BlueSky Social (AT Protocol).

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey.svg)](https://github.com/yourusername/BlueSkyOSINT)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Documentation](#documentation) • [Legal](#legal--ethical-use)

</div>

---

## 🎯 Features

### 21 Powerful OSINT Functions

#### 🔍 **Search Operations** (5 options)
- **Keyword Search** - Search posts across BlueSky network
- **Hashtag Search** - Monitor specific hashtags  
- **Advanced Search** - Filters for language, mentions
- **Trending Posts** - Discover popular content
- **User Mentions** - Find who's talking about specific users

#### 👤 **User Intelligence** (5 options)
- **Profile Analysis** - Complete account metadata
- **Timeline Collection** - Archive user post history
- **Liked Posts** - What users are liking
- **Replies Analysis** - User reply patterns
- **Activity Analysis** - Comprehensive engagement statistics

#### 🕸️ **Network Analysis** (4 options)
- **Get Followers** - Who follows a user
- **Get Following** - Who a user follows
- **Network Mapper** - Compare TWO accounts, find shared connections
- **Community Detection** - Analyze single account's community structure

#### 📡 **Real-time Monitoring** (3 options)
- **User Monitoring** - Track individual accounts
- **Hashtag Monitoring** - Watch trending topics
- **Multi-user Monitoring** - Track multiple accounts simultaneously

#### 💾 **Data Management** (4 options)
- **JSON Export** - Evidence preservation
- **View Cache** - Review collected data
- **Clear Cache** - Reset session data
- **Statistics** - Usage and collection summary

### 🎨 User Interface Features
- **Loading Animations** - Visual feedback during operations
- **Progress Bars** - Track collection progress
- **Emoji Icons** - Intuitive visual indicators
- **Color-coded Output** - Easy-to-read results
- **Animated Separators** - Clean section divisions
- **Status Messages** - Clear success/error indicators

---

## 📋 Requirements

- Python 3.7 or higher
- BlueSky account (for authentication)
- Internet connection

---

## 🚀 Installation

### Quick Install

```bash
# Clone the repository
git clone https://github.com/yourusername/BlueSkyOSINT.git
cd BlueSkyOSINT

# Install dependencies
pip install -r requirements.txt

# Run the tool
python3 blueskyosint.py
```

### Manual Installation

```bash
# Install dependencies manually
pip install atproto colorama

# Run the tool
python3 blueskyosint.py
```

### Using the Install Script

```bash
chmod +x install.sh
./install.sh
```

---

## 🔐 Authentication

BlueSkyOSINT requires authentication with your BlueSky credentials:

```
BlueSky Handle: your.handle.bsky.social
Password: your_password_or_app_password
```

**Security Notes:**
- Credentials are NOT stored
- Only used for the current session
- Consider using [app passwords](https://bsky.app/settings/app-passwords) for extra security
- See [AUTHENTICATION.md](AUTHENTICATION.md) for detailed guide

---

## 📖 Usage

### Basic Operation

```bash
python3 blueskyosint.py
```

You'll see:
1. Custom ASCII art banner
2. Authentication prompt
3. 21-option menu with categories
4. Animated progress indicators

### Example Workflows

#### **Investigate a User**
```
1. Profile User (Option 6)
   → Get account overview

2. Collect Timeline (Option 7)
   → Archive all posts

3. Activity Analysis (Option 10)
   → View engagement statistics

4. Community Detection (Option 14)
   → Understand social structure

5. Export Results (Option 18)
   → Save as JSON
```

#### **Find Connections Between Two Accounts**
```
1. Network Mapper (Option 13)
   → Compare account1 and account2
   → Shows shared followers/following

2. Profile each shared connection
   → Investigate intermediaries
```

#### **Monitor Real-time Activity**
```
1. Monitor User (Option 15)
   → Track specific account

2. Monitor Hashtag (Option 16)
   → Watch trending topics

3. Monitor Multiple Users (Option 17)
   → Track several accounts simultaneously
```

---

## 📚 Documentation

- **[AUTHENTICATION.md](AUTHENTICATION.md)** - Authentication guide and security best practices
- **[NETWORK_ANALYSIS_GUIDE.md](NETWORK_ANALYSIS_GUIDE.md)** - Detailed guide for network analysis features
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute to the project

---

## 🔧 Advanced Usage

### With Tor (OPSEC)

```bash
# Install proxychains4
sudo apt install proxychains4

# Configure for Tor
# Edit /etc/proxychains4.conf
# Add: socks5 127.0.0.1 9050

# Start Tor
sudo service tor start

# Run tool through Tor
proxychains4 python3 blueskyosint.py
```

### JSON Export

All collected data can be exported to JSON:

```json
{
  "type": "profile",
  "data": {
    "handle": "user.bsky.social",
    "display_name": "John Doe",
    "followers": 150,
    "following": 200,
    "posts": 450
  }
}
```

---

## 🛡️ OPSEC Considerations

### Best Practices
- Use VPN/Tor for anonymous access
- Create dedicated BlueSky account for investigations
- Use app passwords instead of main password
- Rotate app passwords regularly
- Export data to encrypted storage
- Review BlueSky's Terms of Service

### Dedicated Investigation Account

**Recommended Setup:**
1. Create new BlueSky account
2. Use throwaway email
3. Generate app password
4. Use only with BlueSkyOSINT
5. Delete account when investigation complete

---

## ⚖️ Legal & Ethical Use

⚠️ **IMPORTANT DISCLAIMERS**

This tool is designed for **legitimate investigative purposes only**:
- ✅ Licensed private investigators
- ✅ Law enforcement (with proper authority)
- ✅ Security researchers
- ✅ Journalists conducting public interest investigations
- ✅ Academic research

### Legal Compliance
- Only accesses publicly available data
- No authentication bypass or exploitation
- Respects AT Protocol's open nature
- User responsible for compliance with local laws

### Prohibited Uses
- ❌ Harassment or stalking
- ❌ Unauthorized surveillance
- ❌ Data scraping for commercial purposes
- ❌ Any activity violating BlueSky Terms of Service
- ❌ Any illegal activities

**By using this tool, you agree to use it responsibly and in compliance with all applicable laws and regulations.**

---

## 🐛 Troubleshooting

### Common Issues

**"atproto library not installed"**
```bash
pip install atproto --break-system-packages
```

**"Authentication failed"**
- Verify credentials
- Check if 2FA is enabled (not supported)
- Try app password instead

**"Network error"**
- Check internet connection
- Try without proxy first
- Verify BlueSky isn't down

**User Not Found**
- Verify handle spelling
- Ensure account is public

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- Report bugs
- Suggest new features
- Improve documentation
- Submit pull requests

---

## 📊 Technical Details

### Dependencies
- `atproto` - Official AT Protocol Python SDK
- `colorama` - Cross-platform terminal colors

### AT Protocol Endpoints Used
- `app.bsky.feed.searchPosts` - Search posts
- `app.bsky.actor.getProfile` - User profiles
- `app.bsky.feed.getAuthorFeed` - User timelines
- `app.bsky.graph.getFollowers` - Followers data
- `app.bsky.graph.getFollows` - Following data

---

## 🗺️ Roadmap

- [ ] Advanced filtering options
- [ ] Media download capability
- [ ] Graph visualization
- [ ] Multi-instance support
- [ ] Batch user analysis
- [ ] Sentiment analysis
- [ ] CSV export format
- [ ] Thread reconstruction
- [ ] Geolocation analysis
- [ ] Historical data comparison

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**OSINTCabal**

- GitHub: [@yourusername](https://github.com/yourusername)
- BlueSky: [@osintcabal.bsky.social](https://bsky.app/profile/osintcabal.bsky.social)

---

## 🌟 Related Projects

- [ChanSINT](https://github.com/yourusername/ChanSINT) - 4chan/8kun OSINT
- [TelegramOSINT-Kit](https://github.com/yourusername/TelegramOSINT) - Telegram Intelligence
- [SneakLeak](https://github.com/yourusername/SneakLeak) - Breach Data Analysis

---

## 📞 Support

For issues, questions, or suggestions:
- Open a [GitHub Issue](https://github.com/yourusername/BlueSkyOSINT/issues)
- Contact: [your contact method]

---

## ⚠️ Disclaimer

This tool is provided "as is" without warranty. The author assumes no liability for misuse or any damages resulting from the use of this software. Users are responsible for ensuring their use complies with all applicable laws and regulations.

---

<div align="center">

**Built for the OSINT Community** 🔍

*Professional intelligence gathering for BlueSky/AT Protocol*

</div>
