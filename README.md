# API to interface with Slack

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
  <td>POST</td>
  <td>/chat/{chat_id}/message</td>
  <td>Post a new message in a chat</td>
</tr>
<tr>
  <td>GET</td>
  <td>/chat/{chat_id}</td>
  <td>Get chat details</td>
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



