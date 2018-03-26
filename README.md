# PyPocket

PyPocket is a project that import some itens from
[pocket](https://getpocket.com/) with a specific tag. It appends
those imported itens into a file named **~/pocket.org**.

It uses **Python 3**.

My configured tag is **export emacs**.

# How to Install

First of all clone this repository.

`git clone https://github.com/chinen93/PyPocket.git`

## Pocket API

[Pocket API](https://getpocket.com/developer/docs/overview) is needed
to use PyPocket.


> The Pocket Authentication API uses a variant of OAuth 2.0 for
> authentication.

### Keys to Access the API

#### First you need a "Consumer Key"

You can get a [consumer key](https://getpocket.com/developer/apps/new)
in the link. If you don't have one.

This project uses a file named **~/pocketKeys.txt** in your home
directory to save and use your pocket authorization. It saves
your *consumer key* and you *authenticated token*.

#### Finally an "Authenticated Token"

Execute the code:

`python3 GetAuthentication.py`

This code has these flows:

- If the file **~/pocketKeys.txt** don't exist. A *consumer key* will
  be asked to the user. Then an *authenticated token* will be
  created. The file is create and those 2 keys are stored.
  
- If the file **~/pocketKeys.txt** does exist but is empty. The first
  item will happen.
  
- If the file **~/pocketKeys.txt** does exist and has the *consumer
  key* and the *authenticated token*. The code doesn't need to to
  anything and just finishes.

## Importing Itens

Execute the code:

`python3 Import.py &optional tag removeTag authenticationFile toFile`

This code has :

- If the `tag` is given the program will retrieve every item from
  [pocket](https://getpocket.com/) with this tag. Default is "export
  emacs". 
  
- If `removeTag` is set to `True` itens will be update. Losing the `tag`
  expecified. Default is `False`.
  
- If `toFile` is defined the itens will be appended to this
  file. Default is "~/pocketItens.org".

- If `authenticationFile` is given the program will get the
  authentication tokens from those files. Default is
  "~/pocketKeys.txt".

