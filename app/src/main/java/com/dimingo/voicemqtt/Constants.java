package com.dimingo.voicemqtt;


public class Constants {

    public static final String MQTT_BROKER_URL = "tcp://broker.emqx.io:1883";

    public static final String MQTT_BROKER_USERNAME = "emqx";
    public static final String MQTT_BROKER_PASSWORD = "public";

    public static final String PUBLISH_TOPIC = "/command";
    public static final String SUBSCRIBE_TOPIC = "/status";

    public static final String CLIENT_ID = "gmandroidmqtt";

    public static final int QOS = 0;
}

