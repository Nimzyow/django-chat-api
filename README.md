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

## Requirements



### API Specifications
<table>
  <tr>
    <th>
      Spec
    </th>
    <th>
      Status
    </th>
  </tr>
  <tr>
    <td>
      Enable one-on-one chat
    </td>
    <td>
      Enabled
    </td>
  </tr>
  <tr>
    <td>
      Enable group chats with multiple people
    </td>
    <td>
      Enabled
    </td>
  </tr>
  <tr>
    <td>
      fetching list of messages
    </td>
    <td>
      Enabled
    </td>
  </tr>
  <tr>
    <td>
      posting messages
    </td>
    <td>
      Enabled
    </td>
  </tr>
  <tr>
    <td>
      deleting messages
    </td>
    <td>
      Enabled
    </td>
  </tr>
  <tr>
    <td>
      check whether messages are read or unread
    </td>
    <td>
      Not enabled
    </td>
  </tr>
  <tr>
    <td>
      Notify necessary users when a message is posted
    </td>
    <td>
      Not enabled
    </td>
  </tr>
  <tr>
    <td>
      User can set notifications to push, email or no notifications
    </td>
    <td>
      Enabled
    </td>
  </tr>
</table>

## Plan

The plan so far is to have the following endpoints.

<table>
  <tr>
    <th>REQUEST</th>
    <th>URL</th>
    <th>BODY</th>
    <th>AUTHORIZATION HEADER REQUIRED</th>
    <th>NOTES</th>
  </tr>
<tr>
  <td>POST</td>
  <td>/users/register</td>
  <td>{"username": "test","password": "testingthisthing","email": "test@example.com"}</td>
  <td></td>
  <td>Creates new user</td>
</tr>
<tr>
  <td>POST</td>
  <td>/users/login</td>
  <td>{"username": "test","password": "testingthisthing"}</td>
  <td></td>
  <td>Logs in and returns token</td>
</tr>
<tr>
  <td>POST</td>
  <td>/chat/open</td>
  <td>{"users": ["user_id_one", "user_id_two"]}</td>
  <td>YES</td>
  <td>Start new chat with users. Chat ID in response</td>
</tr>
<tr>
  <td>GET</td>
  <td>/chat/{chat_id}</td>
  <td>Get chat details</td>
  <td>YES</td>
  <td>Not yet implemented</td>
</tr>
<tr>
  <td>POST</td>
  <td>/chat/{chat_id}/message</td>
  <td>{"text": "random text"}</td>
  <td>YES</td>
  <td>Create new message in channel</td>
</tr>
<tr>
  <td>GET</td>
  <td>/chat/{chat_id}/messages</td>
  <td></td>
  <td>YES</td>
  <td>Get conversation history. Includes "ts" in reponse for deletion of message.</td>
</tr>
<tr>
  <td>DELETE</td>
  <td>/chat/{chat_id}</td>
  <td>{"ts": "12341234.32234"}</td>
  <td>YES</td>
  <td>Delete a specific message from a chat</td>
</tr>
</table>

## Note

After reading Slacks documentation, signing up to slack, creating a bot and assiging permissions for the token

Go to https://api.slack.com/apps

Create app and select app.

Go to OAuth & Permissions. Set Bot Token Scopes:

* app_mentions:read
* channels:history
* channels:join
* channels:manage
* channels:read
* chat:write
* groups:history
* groups:read
* groups:write
* im:history
* im:read
* im:write
* mpim:history
* mpim:read
* mpim:write
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


