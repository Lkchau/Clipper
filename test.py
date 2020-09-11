import clipperTwitch

userlogin= "petergilbz"
B_ID = "69523271"

# query= clipperTwitch.get_user_streams_query(userlogin)
query= clipperTwitch.get_clips_query(B_ID)
# query= clipperTwitch.get_user_query(userlogin)
response= clipperTwitch.get_response(query)

clipperTwitch.print_response(response)