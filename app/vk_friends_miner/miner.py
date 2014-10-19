import api
import output


def get_gml(uid):
    friends_data = api.get_friends_data(uid, fields=['city', 'sex'])
    friend_friends = dict()
    for friend_data in friends_data:
        friend_uid = friend_data['uid']
        friend_friends[friend_uid] = api.get_friend_uids(friend_uid)
        if uid in friend_friends[friend_uid]:
            friend_friends[friend_uid].remove(uid)

    return output.to_glm(friends_data, friend_friends)



