# AlphaSights New Strategy

After extensive research, AlphaSight's Product team figured out that we can significantly improve our relationship with our clients if the links we share with them are shorter because it would make it easier for them to share those links.

## Installing wrapper
gradle wrapper --gradle-version=5.6 --distribution-type=bin

## Building
./gradlew assemble

## Running the application
java -jar build/libs/javashortener-1.0-SNAPSHOT.jar

## Running the tests
./gradlew test
