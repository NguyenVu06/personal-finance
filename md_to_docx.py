import pypandoc

if __name__ == "__main__":
    output = pypandoc.convert_file(r'/Users/nguyendvu/local_repo/personal-finance/vim_qkst.md', 'docx', outputfile="vim_qkst.docx")


