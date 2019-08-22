package com.alphasights.shortener;

//https://github.com/rest-assured/rest-assured/wiki/Usage
import io.restassured.RestAssured;

import org.junit.Test;

public class UrlShortenerTest {

    @Test
    public void testHomeRespondsWith200() {
        RestAssured.baseURI  = "http://localhost:7000";

        RestAssured.given()
            .when()
                .get("/")
            .then()
                .statusCode(200);
    }
}
