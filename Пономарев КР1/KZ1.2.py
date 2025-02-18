a=input()
def camel(st):
    lang="cъешьещёэтихмягкихфранцузскихбулокдавыпейчаю"
    st=st.lower()
    nextl = 1
    for i in range(len(st)):
        if st[i] in lang:
            if nextl == 1:
                st=st[:i]+st[i].upper()+st[i+1:]
                nextl = 0
            else:
                nextl= 1

    return (st)

print(camel(a))
