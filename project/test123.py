with open('k8s_url.txt', 'r', encoding='utf-8') as url_file:
    k8s_url = url_file.readline().strip('\n')

print(k8s_url+'/gal/1')