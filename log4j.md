---
layout: default
---

### log4j

JVM

JAVA_OPTS=

-Dlog4j.debug=true


src/log4j2.xml:
```xml

<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="DEBUG">
    <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} [%t] %-5p %c{1}:%L - %msg%n" />
        </Console>

        <RollingFile name="RollingFile" filename="test.log"
                     filepattern="${logPath}/%d{YYYYMMddHHmmss}-fargo.log">
            <PatternLayout pattern="%d{YYYY-MM-dd HH:mm:ss} [%t] %-5p %c{1}:%L - %msg%n" />
            <Policies>
                <SizeBasedTriggeringPolicy size="300 MB" />
            </Policies>
            <DefaultRolloverStrategy max="20" />
        </RollingFile>

    </Appenders>
    <Loggers>
     <Logger name="net.sf.jasperreports.engine.query.JRJdbcQueryExecuter" level="DEBUG" additivity="true">
            <AppenderRef ref="Console" />
            <AppenderRef ref="RollingFile" />
        </Logger>
    
        <Root level="INFO">
            <AppenderRef ref="Console" />
            <AppenderRef ref="RollingFile" />
        </Root>
    </Loggers>
</Configuration>

```