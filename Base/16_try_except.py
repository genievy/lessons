

# def main():
#     d = {'website': 'google'}
#     try:
#         data = d['url']
#     except:
#         data = 'https://'
#     print(data)
#
# main()

# def main():
#     d = {'website': 'google'}
#     try:
#         print(s)
#         data = d['url']
#     except:
#         print('ooops')
#         data = 'https://'
#         return data
#     finally:
#         print('Very impoitant action')
# result = main()
# print(result)

# def main():
#     d = {'website': 'google', 'url': 'google'}
#     try:
#         data = d['url']
#     except:
#         data = 'https://'
#     else:
#         data = data.upper()
#     print(data)
#
# main()


def main():
    d = {'website': 'google'}
    try:
        print(s)
        data = d['url']
    except NameError:
        print('ooops')
        data = 'https://'
    finally:
        print('Very impoitant action')

result = main()
print(result)
