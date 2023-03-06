mkdir -p /opt/ora/
cd /opt/ora/

wget https://github.com/leonnleite/instant-client-oracle/raw/master/instantclient-basic-linux.x64-12.2.0.1.0.zip
wget https://github.com/leonnleite/instant-client-oracle/raw/master/instantclient-sdk-linux.x64-12.2.0.1.0.zip

unzip instantclient-basic-linux.x64-12.2.0.1.0.zip -d /opt/ora/
unzip instantclient-sdk-linux.x64-12.2.0.1.0.zip -d /opt/ora/

apt-get install -y libaio1
rm -rf /etc/profile.d/oracle.sh
echo "export ORACLE_HOME=/opt/ora/instantclient_12_2" >>/etc/profile.d/oracle.sh
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME" >>/etc/profile.d/oracle.sh
chmod 777 /etc/profile.d/oracle.sh
/bin/bash /etc/profile.d/oracle.sh
env | grep -i ora # This will check current ENVIRONMENT settings for Oracle

rm -rf /etc/ld.so.conf.d/oracle.conf
echo "/opt/ora/instantclient_12_2" >>/etc/ld.so.conf.d/oracle.conf
ldconfig
cd $ORACLE_HOME

ln -s libclntsh.so.12.1 libclntsh.so

cd /app
