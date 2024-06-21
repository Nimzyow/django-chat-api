# API to interface with Slack

## Setup

```bash
# Create a python environment

python3 -m venv .venv

source ./.venv/bin/activate
```

```bash
# Install dependencies

pip install -r requirements.txt
```

You will need to create a params.ini file. 

Copy `params_example.ini` and rename new file to `params.ini`.

inside `params.ini`, set `YOUR_SLACK_TOKEN` to your slack token.

## Plan

The plan so far is to have the following endpoints.

<table>
  <tr>
    <th>REQUEST</th>
    <th>API</th>
    <th>NOTES</th>
  </tr>
<tr>
  <td>POST</td>
  <td>/chat</td>
  <td>Start new chat</td>
</tr>
<tr>
  <td>GET</td>
  <td>/chat/{chat_id}</td>
  <td>Get chat details</td>
</tr>
<tr>
  <td>POST</td>
  <td>/chat/{chat_id}/message</td>
  <td>Post a new message in a chat</td>
</tr>
<tr>
  <td>GET</td>
  <td>/chat/{chat_id}/messages</td>
  <td>Get all messages in a chat</td>
</tr>
<tr>
  <td>DELETE</td>
  <td>/chat/{chat_id}/messages/{message_id}</td>
  <td>Delete a specific message from a chat</td>
</tr>
</table>

## Note

Take into consideration auth. Most likely we'll need to gain a token of some sorts. Possibly:
 
  * /auth/login

We will retrieve the token and send it through the body of any request. I'm just guessing that's how the Slack API works at this point.

After reading Slacks documentation, signing up to slack, creating a bot and assiging permissions for the token

Go to https://api.slack.com/apps

Create app and select app.

Go to OAuth & Permissions. Set Bot Token Scopes:

* app_mentions:read
* channels:history
* channels:join
* channels:read
* chat:write
* im:read
* users.profile:read
* users:read

We need to get a channel ID to post a message to

```
GET https://slack.com/api/conversations.list?=

Headers:
  - Authorization:  Bearer MY_TOKEN

Output:
{
    "ok": true,
    "channel": {
        "id": "CHANNEL_ID",
        "name": "best-project",
        ...

```

The bot needs to join a channel

```
POST https://slack.com/api/conversations.join

Headers:
  - Content-Type:   application/json
  - Authorization:  Bearer MY_TOKEN

body = {
    "channel": "CHANNEL_ID"
}
```

Then the bot can send a message to a channel

```
POST https://slack.com/api/chat.postMessage

Headers:
  - Content-Type:   application/json
  - Authorization:  Bearer MY_TOKEN

body {
    "channel": "CHANNEL_ID",
    "text": "Hello world!"
}
```
Note: CHANNEL_ID can be replaced with a user id to send a DM to a user.

We'll utilise the python slack SDK to make the above calls. Each call will be contained in their relevant view.


