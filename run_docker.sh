clear
sudo docker-compose rm -f
docker-compose pull
sudo db_username='root' db_password='root@1234' mail_id='balaji@ibhut.com' mail_password='lbeHgE3a0exkoo9b' TWILIO_ACCOUNT_SID='ACdcac30644d7d6c29585cae0aa5062966' TWILIO_AUTH_TOKEN='7de96942e2fb482338a5b4c85e80865a' SERVICE_SID='VAfb7f0ecacf89e46d293cd8e7860f1aa5' ACCESS_SECRET="9yaB&E)H@McQfTjWnZq4t7w!z%C*FtJa" REFRESH_SECRET="PdSgVkYp2s5v8y/B?E(H+MbQeThWmZq4" docker-compose up --remove-orphans --no-deps