def accountsMerge(accounts):

    from queue import Queue

    answer = []
    n = len(accounts)
    visited = [False] * n
    # email address to user id
    mail_to_id = dict()
    for user_id, account in enumerate(accounts):
        for email in account[1:]:
            if email in mail_to_id:
                mail_to_id[email].append(user_id)
            else:
                mail_to_id[email] = [user_id]
    # print(mail_to_id)
    # Begin BFS, for each user, we first push its ID into queue.
    # Then for all the ID popped by the queue, we check its email address,
    # and find the related other user by mail_to_id. Push the related users
    # into the queue
    for i in range(n):
        if visited[i]:
            continue
        bfs = Queue()
        bfs.put(i)
        visited[i] = True
        this_user_email = set() # The (unique) email address of this user
        while not bfs.empty():
            cur_user_id = bfs.get()
            # print(cur_user_id)
            # if visited[cur_user_id]:
            #     continue
            visited[cur_user_id] = True
            # User's email addresses are iterated.
            # Find the next user by mail_to_id
            for email in accounts[cur_user_id][1: ]:
                this_user_email.add(email)
                for next_user_id in mail_to_id[email]:
                    if visited[next_user_id]:
                        continue
                    bfs.put(next_user_id)
                    visited[next_user_id] = True
        this_answer = list(this_user_email)
        this_answer.sort()
        this_answer.insert(0, accounts[i][0])
        answer.append(this_answer)

    return answer

print(accountsMerge(accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))