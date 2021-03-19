global_init(input())
db_sess = create_session()
for user in db_sess.query(User).filter(
        User.address.like("%1%"), User.speciality.notlike("%engineer%"), User.position.notlike("%engineer%")):
    print(user.id)
