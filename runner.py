from hello import app
import os
if __name__ == '__main__':
    app.run(debug=True,port=8080,host=os.environ["IP"])
    