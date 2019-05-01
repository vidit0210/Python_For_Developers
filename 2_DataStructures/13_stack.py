browsing_session = []
browsing_session.append('udacity')
browsing_session.append('reddit')
browsing_session.append('udemy')
print(browsing_session.pop())
browsing_session.pop()
browsing_session.pop()


if not browsing_session:
    print('Disabled')
