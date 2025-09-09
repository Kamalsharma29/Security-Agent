# Security Agent for Agentverse

A powerful security monitoring agent that integrates with Fetch.ai's Agentverse platform to provide URL safety checking and collaborative threat detection.

## 🚀 Features

- **URL Safety Analysis**: Real-time URL scanning using Google Safe Browsing API
- **Agentverse Integration**: Seamless connection to Fetch.ai's decentralized agent network
- **Chat Protocol**: Interactive communication through Agentverse chat interface
- **Threat Detection**: Identifies malware, social engineering, and unwanted software
- **Agent Collaboration**: Can communicate with other security agents on the network

## 📋 Prerequisites

- Python 3.8 or higher
- Google Safe Browsing API key
- Internet connection for Agentverse integration

## 🛠️ Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install uagents python-dotenv requests
   ```

3. **Set up environment variables**:
   - Copy `.env.template` to `.env`
   - Add your Google Safe Browsing API key:
     ```
     SAFE_BROWSING_API_KEY=your_api_key_here
     ```

## 🔑 Getting API Keys

### Google Safe Browsing API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Safe Browsing API
4. Create credentials (API Key)
5. Copy the API key to your `.env` file

## 🚀 Usage

### Running the Agent

```bash
python security_agent.py
```

The agent will start and display:
- Local server URL: `http://0.0.0.0:8002`
- Agent address for identification
- Agentverse inspector URL for web interface

### Accessing the Chat Interface

1. **Via Agent Inspector**:
   - Use the inspector URL shown in the terminal
   - Example: `https://agentverse.ai/inspect/?uri=http%3A//127.0.0.1%3A8002&address=agent1q...`

2. **Via Agentverse Dashboard**:
   - Visit [https://agentverse.ai](https://agentverse.ai)
   - Sign in to your account
   - Find your "Security-Agent" in the dashboard
   - Click to open the chat interface

### Testing URL Safety

Send URLs to the agent through the chat interface:

**Safe URL Example**:
```
https://google.com
```
**Response**: ✅ The URL `https://google.com` seems **safe**.

**Unsafe URL Example**:
```
http://malicious-site.example
```
**Response**: ⚠️ ALERT: The URL `http://malicious-site.example` is flagged as **unsafe**!

## 🏗️ Project Structure

```
security agent/
├── security_agent.py      # Main agent code
├── .env                   # Environment variables (create from template)
├── .env.template         # Environment template
└── README.md            # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SAFE_BROWSING_API_KEY` | Google Safe Browsing API key | Yes |

### Agent Settings

- **Agent Name**: Security-Agent
- **Port**: 8002
- **Mailbox**: Enabled for Agentverse communication
- **Protocol**: Chat protocol for interactive communication

## 🛡️ Security Features

### Threat Detection
The agent checks URLs against Google's Safe Browsing database for:
- **Malware**: Malicious software downloads
- **Social Engineering**: Phishing and deceptive sites
- **Unwanted Software**: Potentially harmful applications
- **Harmful Applications**: Apps that may compromise security

### Response Format
- ✅ **Safe URLs**: Clear confirmation of safety
- ⚠️ **Unsafe URLs**: Detailed threat information
- ❌ **Invalid URLs**: Guidance for proper URL format

## 🤝 Agent Collaboration

This agent is designed to work with other security agents on Agentverse:
- **Threat Intelligence Sharing**: Exchange security information
- **Collaborative Analysis**: Work together on complex threats
- **Network Security**: Distributed security monitoring

## 📊 Monitoring and Logs

The agent provides detailed logging:
- Connection status to Agentverse
- URL analysis results
- Agent registration information
- Error handling and debugging info

## 🔍 Troubleshooting

### Common Issues

1. **Chat option not showing in Agentverse**:
   - Wait a few minutes after agent startup
   - Refresh the Agentverse page
   - Check agent registration logs

2. **API key errors**:
   - Verify your Google Safe Browsing API key
   - Check API quotas and limits
   - Ensure the API is enabled in Google Cloud Console

3. **Connection issues**:
   - Check internet connectivity
   - Verify firewall settings for port 8002
   - Ensure Agentverse services are accessible

### Debug Mode

For detailed debugging, check the terminal output when running the agent. Look for:
- `INFO` messages for successful operations
- `WARNING` messages for potential issues
- `ERROR` messages for problems requiring attention

## 🚀 Advanced Usage

### Custom Modifications

You can extend the agent by:
- Adding more threat intelligence sources
- Implementing file hash checking
- Adding email or Slack notifications
- Creating custom security rules

### Integration with Other Agents

This agent can communicate with:
- Network monitoring agents
- File system security agents
- Incident response agents
- Threat intelligence agents

## 📝 API Reference

### Message Types

- **ChatMessage**: Send URLs for analysis
- **ChatAcknowledgement**: Confirm message receipt
- **TextContent**: Plain text communication

### Response Codes

- **Safe URL**: No threats detected
- **Unsafe URL**: Threats found with details
- **Invalid Format**: URL format error
- **API Error**: Service unavailable

## 🤝 Contributing

To contribute to this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Please check the license file for details.

## 🆘 Support

For support:
- Check the troubleshooting section
- Review Agentverse documentation
- Contact the development team

## 🔗 Useful Links

- [Fetch.ai Documentation](https://docs.fetch.ai/)
- [Agentverse Platform](https://agentverse.ai/)
- [Google Safe Browsing API](https://developers.google.com/safe-browsing)
- [uAgents Framework](https://github.com/fetchai/uAgents)

---

**Made with ❤️ for the Fetch.ai ecosystem**