from mastodon import Mastodon

Mastodon.create_app(
    'gacha_bot_app',
    api_base_url='https://forgetyounot.pics',
    to_file='clientcred.secret'
)

mastodon = Mastodon(
    client_id='clientcred.secret',
    api_base_url='https://forgetyounot.pics'
)

mastodon.log_in(
    'kokek23520@exitbit.com',   # 여기에 이메일
    'mung0515',                # 여기에 비밀번호
    to_file='usercred.secret',
    scopes=['read', 'write', 'push', 'follow']
)

print("✅ 인증 성공! usercred.secret 파일이 생성되었습니다.")
