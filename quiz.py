import streamlit as st
import random

st.title("手話クイズ٩( 'ω' )و")

# 単語と動画の辞書
quiz_data = {
    "アイロン": "iron.mov",
    "あさって": "asatte.mov",
    "紫陽花": "ajisai.mov",
    "あとで": "atode.mov",
}

# セッションステート初期化
if "current_question" not in st.session_state:
    word, video = random.choice(list(quiz_data.items()))
    st.session_state.current_question = word
    st.session_state.current_video = video
    st.session_state.answered = False
    st.session_state.answer_result = ""
    options = list(quiz_data.keys())
    random.shuffle(options)
    st.session_state.options = options  # 選択肢も固定！

# 動画表示
video_file = open(st.session_state.current_video, 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# クイズ画面
if not st.session_state.answered:
    with st.form("quiz_form"):
        answer = st.radio("これは何の手話でしょう？", st.session_state.options)
        submitted = st.form_submit_button("答える")

        if submitted:
            correct = st.session_state.current_question
            if answer == correct:
                st.session_state.answer_result = "✅ 正解！٩( 'ω' )و"
            else:
                st.session_state.answer_result = f"❌ ぶぶー！正解は「{correct}」だったよ！"
            st.session_state.answered = True
            st.experimental_rerun()

# 結果画面
else:
    st.markdown(f"### {st.session_state.answer_result}")
    if st.button("次の問題へ"):
        word, video = random.choice(list(quiz_data.items()))
        st.session_state.current_question = word
        st.session_state.current_video = video
        st.session_state.answered = False
        st.session_state.answer_result = ""
        options = list(quiz_data.keys())
        random.shuffle(options)
        st.session_state.options = options
        st.experimental_rerun()