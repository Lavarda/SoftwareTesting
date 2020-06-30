from blog import Blog
from post import Post

blogs = dict() # blog_name : blog_object
MENU_PROMPT = 'Escreva "c" para criar um blog, "1" para listar os blogs, "r" para ler um, "p" para criar um post e "q" para sair: '
ASK_TITLE_BLOG = 'Escreva o titulo do blog: '
ASK_AUTHOR_BLOG = 'Escreva o author do blog: '
POST_TEMPLATE = '''
--- {} ---

{}

'''
ASK_TITLE_POST = 'Escreva o titulo do post: '
ASK_CONTENT_POST = 'Escreva o titulo do conteúdo do seu blog: '

def menu():
    # Mostrar ao usuario os blogs disponiveis
    # Deixar ele escolher
    # Fazer algo com a escolha
    # Sair
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == '1':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    # Printar os blogs disponiveis
    for key, blog in blogs.items() :
        print('- {}'.format(blog))

def ask_create_blog():
    title_blog = input(ASK_TITLE_BLOG)
    author_blog = input(ASK_AUTHOR_BLOG)
    blogs[title_blog] = Blog(title_blog, author_blog)
    print("Blog criado com sucesso: {}".format(blogs[title_blog]))


def ask_read_blog():
    title_blog = input(ASK_TITLE_BLOG)
    print_posts(blogs[title_blog])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_title = input(ASK_TITLE_BLOG)
    title_post = input(ASK_TITLE_POST)
    content_post = input(ASK_CONTENT_POST)

    blogs[blog_title].create_post(title_post, content_post)
    print("Post escrito com sucesso: {}".format(blogs[blog_title]))
