### .env 는 replit 에서 안돌아가서 해당 서비스에서 제공하는 secrets를 사용함
## source ~/.bashrc 
## venv, run 이용 가능
## alias
## alias venv='source env/bin/activate';alias run='python main.py';
alias start='streamlit run --server.address 0.0.0.0 --server.headless true --server.enableCORS=false --server.enableWebsocketCompression=false --server.runOnSave=false Home.py'


하고 run 누르면 웹뷰가 보이네 ;; ㅋㅋ



streamlit run --server.address 0.0.0.0 --server.headless true --server.enableCORS=false --server.enableWebsocketCompression=false --server.runOnSave=false Home.py