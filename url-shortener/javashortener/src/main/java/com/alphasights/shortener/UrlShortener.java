package com.alphasights.shortener;

import io.javalin.Javalin;

public class UrlShortener {
    public static void main(String[] args) {
        Javalin app = Javalin.create().start(7000);
        app.get("/", ctx -> ctx.result("Welcome to AlphaSights Superday!"));
    }
}
