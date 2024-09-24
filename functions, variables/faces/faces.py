

def convert(faces):
    return faces.replace(":)","🙂").replace(":(","🙁")


def main():
    usr_input=input()
    make_it_emotional= convert(usr_input)
    print(make_it_emotional)
main()