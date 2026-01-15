#!/usr/bin/env python3
"""
BlueSkyOSINT - BlueSky Intelligence Gathering Tool
Similar to ChanSINT but for BlueSky/AT Protocol
"""

import json
import time
import os
from datetime import datetime
from colorama import Fore, Back, Style, init

try:
    from atproto import Client
except ImportError:
    print("[!] Error: atproto library not installed")
    print("[!] Install with: pip install atproto")
    exit(1)

# Initialize colorama
init(autoreset=True)

class BlueSkyOSINT:
    def __init__(self):
        self.client = None
        self.authenticated = False
        self.results = []
        
    def print_banner(self):
        """Display ASCII banner"""
        art = f"""{Fore.CYAN}
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
{Style.RESET_ALL}"""

        text = r"""{}
  ___  ____ ___ _   _ _____ ____  _          
 / _ \/ ___|_ _| \ | |_   _/ ___|| | ___   _ 
| | | \___ \| ||  \| | | | \___ \| |/ / | | |
| |_| |___) | || |\  | | |  ___) |   <| |_| |
 \___/|____/___|_| \_| |_| |____/|_|\_\\__, |
                                       |___/ 
{}""".format(Fore.GREEN, Style.RESET_ALL)

        info = f"""
{Fore.YELLOW}[!] BlueSky OSINT Intelligence Tool - AT Protocol Edition
[!] Authentication Required - Login with BlueSky Credentials
[!] For Investigative Use Only{Style.RESET_ALL}
"""
        print(art + text + info)
        
    def login(self):
        """Authenticate with BlueSky credentials"""
        print(f"\n{Fore.GREEN}═══ AUTHENTICATION REQUIRED ═══{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Enter your BlueSky credentials{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[!] Credentials are NOT stored, only used for this session{Style.RESET_ALL}\n")
        
        while not self.authenticated:
            try:
                handle = input(f"{Fore.CYAN}BlueSky Handle (e.g., user.bsky.social): {Style.RESET_ALL}").strip()
                
                if not handle:
                    print(f"{Fore.RED}[!] Handle required{Style.RESET_ALL}")
                    continue
                
                # Use getpass for password
                import getpass
                password = getpass.getpass(f"{Fore.CYAN}Password: {Style.RESET_ALL}")
                
                if not password:
                    print(f"{Fore.RED}[!] Password required{Style.RESET_ALL}")
                    continue
                
                print(f"\n{Fore.YELLOW}[*] Authenticating...{Style.RESET_ALL}")
                
                # Create client and login
                self.client = Client()
                self.client.login(handle, password)
                
                self.authenticated = True
                print(f"{Fore.GREEN}[+] Successfully authenticated as @{handle}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}[+] Session established{Style.RESET_ALL}\n")
                
                return True
                
            except Exception as e:
                print(f"{Fore.RED}[!] Authentication failed: {e}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}[*] Please try again or press Ctrl+C to exit{Style.RESET_ALL}\n")
                self.authenticated = False
        
    def main_menu(self):
        """Display main menu"""
        print(f"\n{Fore.GREEN}═══ MAIN MENU ═══{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[1]{Style.RESET_ALL} Search Posts by Keyword")
        print(f"{Fore.CYAN}[2]{Style.RESET_ALL} Profile User (by handle)")
        print(f"{Fore.CYAN}[3]{Style.RESET_ALL} Collect User Timeline")
        print(f"{Fore.CYAN}[4]{Style.RESET_ALL} Monitor User Activity")
        print(f"{Fore.CYAN}[5]{Style.RESET_ALL} Search by Hashtag")
        print(f"{Fore.CYAN}[6]{Style.RESET_ALL} Network Analysis (Followers)")
        print(f"{Fore.CYAN}[7]{Style.RESET_ALL} Export Results to JSON")
        print(f"{Fore.CYAN}[8]{Style.RESET_ALL} View Cached Results")
        print(f"{Fore.RED}[0]{Style.RESET_ALL} Exit")
        print(f"{Fore.GREEN}{'═' * 30}{Style.RESET_ALL}")
        
    def search_posts(self, query, limit=50):
        """Search posts by keyword"""
        if not self.authenticated:
            print(f"{Fore.RED}[!] Not authenticated. Please restart and login.{Style.RESET_ALL}")
            return []
        
        print(f"\n{Fore.YELLOW}[*] Searching for: '{query}'{Style.RESET_ALL}")
        
        try:
            # Use atproto client to search
            response = self.client.app.bsky.feed.search_posts({'q': query, 'limit': limit})
            
            posts = response.posts if hasattr(response, 'posts') else []
            
            if not posts:
                print(f"{Fore.RED}[!] No posts found{Style.RESET_ALL}")
                return []
            
            print(f"{Fore.GREEN}[+] Found {len(posts)} posts{Style.RESET_ALL}\n")
            
            results = []
            for idx, post in enumerate(posts, 1):
                post_data = self.parse_post(post)
                results.append(post_data)
                
                print(f"{Fore.CYAN}{'─' * 70}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}[{idx}] Post by: @{post_data['author']}{Style.RESET_ALL}")
                print(f"{Fore.WHITE}Date: {post_data['created_at']}{Style.RESET_ALL}")
                print(f"{Fore.WHITE}Text: {post_data['text'][:200]}...{Style.RESET_ALL}" if len(post_data['text']) > 200 else f"{Fore.WHITE}Text: {post_data['text']}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}❤️  {post_data['likes']} | 🔄 {post_data['reposts']} | 💬 {post_data['replies']}{Style.RESET_ALL}")
                print(f"{Fore.BLUE}URI: {post_data['uri']}{Style.RESET_ALL}")
            
            self.results.extend(results)
            return results
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
            return []
    
    def get_profile(self, handle):
        """Get user profile information"""
        if not self.authenticated:
            print(f"{Fore.RED}[!] Not authenticated. Please restart and login.{Style.RESET_ALL}")
            return None
        
        print(f"\n{Fore.YELLOW}[*] Fetching profile: @{handle}{Style.RESET_ALL}")
        
        try:
            # Clean handle
            handle = handle.replace('@', '')
            
            # Use atproto client
            profile = self.client.app.bsky.actor.get_profile({'actor': handle})
            
            print(f"\n{Fore.GREEN}{'═' * 70}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}PROFILE: @{profile.handle}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{'═' * 70}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Display Name: {profile.display_name or 'N/A'}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}DID: {profile.did}{Style.RESET_ALL}")
            print(f"{Fore.WHITE}Description: {profile.description or 'N/A'}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Followers: {profile.followers_count or 0} | Following: {profile.follows_count or 0}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Posts: {profile.posts_count or 0}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{'═' * 70}{Style.RESET_ALL}")
            
            profile_data = {
                'handle': profile.handle,
                'display_name': profile.display_name,
                'did': profile.did,
                'description': profile.description,
                'followers': profile.followers_count or 0,
                'following': profile.follows_count or 0,
                'posts': profile.posts_count or 0,
                'avatar': getattr(profile, 'avatar', None),
                'banner': getattr(profile, 'banner', None),
                'retrieved_at': datetime.now().isoformat()
            }
            
            self.results.append({'type': 'profile', 'data': profile_data})
            return profile_data
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
            return None
    
    def get_user_posts(self, handle, limit=50):
        """Collect user's timeline/posts"""
        if not self.authenticated:
            print(f"{Fore.RED}[!] Not authenticated. Please restart and login.{Style.RESET_ALL}")
            return []
        
        print(f"\n{Fore.YELLOW}[*] Collecting posts from: @{handle}{Style.RESET_ALL}")
        
        try:
            handle = handle.replace('@', '')
            
            # Use atproto client
            feed = self.client.app.bsky.feed.get_author_feed({'actor': handle, 'limit': limit})
            
            posts = feed.feed if hasattr(feed, 'feed') else []
            
            if not posts:
                print(f"{Fore.RED}[!] No posts found{Style.RESET_ALL}")
                return []
            
            print(f"{Fore.GREEN}[+] Collected {len(posts)} posts{Style.RESET_ALL}\n")
            
            results = []
            for idx, item in enumerate(posts, 1):
                post = item.post
                post_data = self.parse_post(post)
                results.append(post_data)
                
                print(f"{Fore.CYAN}[{idx}] {post_data['created_at']}{Style.RESET_ALL}")
                print(f"    {post_data['text'][:100]}..." if len(post_data['text']) > 100 else f"    {post_data['text']}")
                print(f"    {Fore.GREEN}❤️  {post_data['likes']} | 🔄 {post_data['reposts']} | 💬 {post_data['replies']}{Style.RESET_ALL}")
            
            timeline_data = {
                'type': 'user_timeline',
                'handle': handle,
                'posts': results,
                'count': len(results),
                'collected_at': datetime.now().isoformat()
            }
            
            self.results.append(timeline_data)
            return results
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
            return []
    
    def monitor_user(self, handle, interval=60, duration=300):
        """Monitor user for new posts"""
        if not self.authenticated:
            print(f"{Fore.RED}[!] Not authenticated. Please restart and login.{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.YELLOW}[*] Monitoring @{handle} for new posts{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Check interval: {interval}s | Duration: {duration}s{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[*] Press Ctrl+C to stop monitoring{Style.RESET_ALL}\n")
        
        handle = handle.replace('@', '')
        seen_posts = set()
        start_time = time.time()
        
        try:
            while (time.time() - start_time) < duration:
                feed = self.client.app.bsky.feed.get_author_feed({'actor': handle, 'limit': 10})
                posts = feed.feed if hasattr(feed, 'feed') else []
                
                for item in posts:
                    post = item.post
                    post_uri = post.uri
                    
                    if post_uri and post_uri not in seen_posts:
                        seen_posts.add(post_uri)
                        post_data = self.parse_post(post)
                        
                        print(f"{Fore.GREEN}[+] NEW POST DETECTED!{Style.RESET_ALL}")
                        print(f"{Fore.CYAN}Time: {post_data['created_at']}{Style.RESET_ALL}")
                        print(f"{Fore.WHITE}Text: {post_data['text']}{Style.RESET_ALL}")
                        print(f"{Fore.BLUE}URI: {post_data['uri']}{Style.RESET_ALL}\n")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Monitoring stopped by user{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
    
    def search_hashtag(self, hashtag, limit=50):
        """Search posts by hashtag"""
        if not hashtag.startswith('#'):
            hashtag = f"#{hashtag}"
        
        print(f"\n{Fore.YELLOW}[*] Searching hashtag: {hashtag}{Style.RESET_ALL}")
        return self.search_posts(hashtag, limit)
    
    def get_followers(self, handle, limit=50):
        """Get user's followers"""
        if not self.authenticated:
            print(f"{Fore.RED}[!] Not authenticated. Please restart and login.{Style.RESET_ALL}")
            return []
        
        print(f"\n{Fore.YELLOW}[*] Fetching followers for: @{handle}{Style.RESET_ALL}")
        
        try:
            handle = handle.replace('@', '')
            
            # Use atproto client
            result = self.client.app.bsky.graph.get_followers({'actor': handle, 'limit': limit})
            
            followers = result.followers if hasattr(result, 'followers') else []
            
            if not followers:
                print(f"{Fore.RED}[!] No followers data available{Style.RESET_ALL}")
                return []
            
            print(f"{Fore.GREEN}[+] Found {len(followers)} followers{Style.RESET_ALL}\n")
            
            followers_list = []
            for idx, follower in enumerate(followers, 1):
                print(f"{Fore.CYAN}[{idx}] @{follower.handle}{Style.RESET_ALL}")
                if follower.display_name:
                    print(f"    {Fore.WHITE}Name: {follower.display_name}{Style.RESET_ALL}")
                if hasattr(follower, 'description') and follower.description:
                    desc = follower.description[:80]
                    print(f"    {Fore.WHITE}{desc}...{Style.RESET_ALL}" if len(follower.description) > 80 else f"    {Fore.WHITE}{desc}{Style.RESET_ALL}")
                
                followers_list.append({
                    'handle': follower.handle,
                    'display_name': follower.display_name,
                    'did': follower.did,
                    'description': getattr(follower, 'description', None)
                })
            
            network_data = {
                'type': 'followers',
                'target_handle': handle,
                'followers': followers_list,
                'count': len(followers_list),
                'collected_at': datetime.now().isoformat()
            }
            
            self.results.append(network_data)
            return followers_list
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
            return []
    
    def parse_post(self, post):
        """Parse post data into standardized format"""
        # Handle both dict and object types
        if hasattr(post, 'record'):
            # atproto object
            record = post.record
            author = post.author if hasattr(post, 'author') else None
            
            return {
                'uri': post.uri,
                'cid': post.cid,
                'author': author.handle if author else 'unknown',
                'author_did': author.did if author else 'unknown',
                'author_display_name': author.display_name if author and hasattr(author, 'display_name') else None,
                'text': record.text if hasattr(record, 'text') else '',
                'created_at': record.created_at if hasattr(record, 'created_at') else None,
                'likes': post.like_count if hasattr(post, 'like_count') else 0,
                'reposts': post.repost_count if hasattr(post, 'repost_count') else 0,
                'replies': post.reply_count if hasattr(post, 'reply_count') else 0,
                'embed': getattr(record, 'embed', None),
                'langs': getattr(record, 'langs', []),
                'retrieved_at': datetime.now().isoformat()
            }
        else:
            # Fallback for dict format
            record = post.get('record', {})
            author = post.get('author', {})
            
            return {
                'uri': post.get('uri'),
                'cid': post.get('cid'),
                'author': author.get('handle'),
                'author_did': author.get('did'),
                'author_display_name': author.get('displayName'),
                'text': record.get('text', ''),
                'created_at': record.get('createdAt'),
                'likes': post.get('likeCount', 0),
                'reposts': post.get('repostCount', 0),
                'replies': post.get('replyCount', 0),
                'embed': record.get('embed'),
                'langs': record.get('langs', []),
                'retrieved_at': datetime.now().isoformat()
            }
    
    def export_to_json(self, filename=None):
        """Export all results to JSON"""
        if not self.results:
            print(f"{Fore.RED}[!] No results to export{Style.RESET_ALL}")
            return
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"bluesky_osint_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            
            print(f"{Fore.GREEN}[+] Results exported to: {filename}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}[+] Total records: {len(self.results)}{Style.RESET_ALL}")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Export error: {e}{Style.RESET_ALL}")
    
    def view_cached_results(self):
        """Display summary of cached results"""
        if not self.results:
            print(f"{Fore.RED}[!] No cached results{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.GREEN}{'═' * 70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}CACHED RESULTS SUMMARY{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'═' * 70}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Total cached items: {len(self.results)}{Style.RESET_ALL}\n")
        
        for idx, result in enumerate(self.results, 1):
            result_type = result.get('type', 'unknown')
            print(f"{Fore.CYAN}[{idx}] {result_type.upper()}{Style.RESET_ALL}")
            
            if result_type == 'profile':
                data = result.get('data', {})
                print(f"    @{data.get('handle')} - {data.get('posts')} posts")
            elif result_type == 'user_timeline':
                print(f"    @{result.get('handle')} - {result.get('count')} posts")
            elif result_type == 'followers':
                print(f"    @{result.get('target_handle')} - {result.get('count')} followers")
            else:
                print(f"    Data items: {len(result) if isinstance(result, list) else 1}")
        
        print(f"{Fore.GREEN}{'═' * 70}{Style.RESET_ALL}")
    
    def run(self):
        """Main program loop"""
        self.print_banner()
        
        # Require authentication before proceeding
        if not self.login():
            print(f"{Fore.RED}[!] Authentication required to use BlueSkyOSINT{Style.RESET_ALL}")
            return
        
        while True:
            self.main_menu()
            
            try:
                choice = input(f"\n{Fore.CYAN}Select option: {Style.RESET_ALL}").strip()
                
                if choice == '1':
                    query = input(f"{Fore.YELLOW}Enter search term: {Style.RESET_ALL}").strip()
                    if query:
                        limit = input(f"{Fore.YELLOW}Max results (default 50): {Style.RESET_ALL}").strip()
                        limit = int(limit) if limit.isdigit() else 50
                        self.search_posts(query, limit)
                
                elif choice == '2':
                    handle = input(f"{Fore.YELLOW}Enter handle (e.g. user.bsky.social): {Style.RESET_ALL}").strip()
                    if handle:
                        self.get_profile(handle)
                
                elif choice == '3':
                    handle = input(f"{Fore.YELLOW}Enter handle: {Style.RESET_ALL}").strip()
                    if handle:
                        limit = input(f"{Fore.YELLOW}Max posts (default 50): {Style.RESET_ALL}").strip()
                        limit = int(limit) if limit.isdigit() else 50
                        self.get_user_posts(handle, limit)
                
                elif choice == '4':
                    handle = input(f"{Fore.YELLOW}Enter handle to monitor: {Style.RESET_ALL}").strip()
                    if handle:
                        interval = input(f"{Fore.YELLOW}Check interval in seconds (default 60): {Style.RESET_ALL}").strip()
                        interval = int(interval) if interval.isdigit() else 60
                        duration = input(f"{Fore.YELLOW}Monitor duration in seconds (default 300): {Style.RESET_ALL}").strip()
                        duration = int(duration) if duration.isdigit() else 300
                        self.monitor_user(handle, interval, duration)
                
                elif choice == '5':
                    hashtag = input(f"{Fore.YELLOW}Enter hashtag (with or without #): {Style.RESET_ALL}").strip()
                    if hashtag:
                        limit = input(f"{Fore.YELLOW}Max results (default 50): {Style.RESET_ALL}").strip()
                        limit = int(limit) if limit.isdigit() else 50
                        self.search_hashtag(hashtag, limit)
                
                elif choice == '6':
                    handle = input(f"{Fore.YELLOW}Enter handle: {Style.RESET_ALL}").strip()
                    if handle:
                        limit = input(f"{Fore.YELLOW}Max followers (default 50): {Style.RESET_ALL}").strip()
                        limit = int(limit) if limit.isdigit() else 50
                        self.get_followers(handle, limit)
                
                elif choice == '7':
                    filename = input(f"{Fore.YELLOW}Filename (press Enter for auto): {Style.RESET_ALL}").strip()
                    self.export_to_json(filename if filename else None)
                
                elif choice == '8':
                    self.view_cached_results()
                
                elif choice == '0':
                    print(f"\n{Fore.GREEN}[+] Exiting BlueSkyOSINT...{Style.RESET_ALL}")
                    break
                
                else:
                    print(f"{Fore.RED}[!] Invalid option{Style.RESET_ALL}")
                
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
                
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}[!] Interrupted by user{Style.RESET_ALL}")
                break
            except Exception as e:
                print(f"{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
                input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")

def main():
    tool = BlueSkyOSINT()
    tool.run()

if __name__ == "__main__":
    main()
