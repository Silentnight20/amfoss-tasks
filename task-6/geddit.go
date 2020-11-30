package main

import (
	"context"
	"fmt"
	"log"

	"github.com/vartanbeno/go-reddit/reddit"
)

var ctx = context.Background()

func main() {
	if err := run(); err != nil {
		log.Fatal(err)
	}
}

func run() (err error) {
	/*
		withCredentials := reddit.WithCredentials("DBaoUj7jOQ9TzQ", "R0Wp5yKqBueahWIwVUxQpN3l8CWtJQ", "thunderbeast_21", "amfossgeddit")
		client, _ := reddit.NewClient(withCredentials) */

	sr, _, err := reddit.DefaultClient().Subreddit.Get(ctx, "golang")
	if err != nil {
		return
	}

	fmt.Printf("%s was created on %s and has %d subscribers.\n", sr.NamePrefixed, sr.Created.Local(), sr.Subscribers)
	return
	
	posts, resp, err := reddit.DefaultClient().Subreddit.TopPosts(ctx, "golang", &reddit.ListPostOptions{
		ListOptions: reddit.ListOptions{
			Limit: 100,
		},
		Time: "all",
	})
	if err != nil {
		return
	}

	for _, post := range posts {
		fmt.Println(post.Title)
	}

	// The After option sets the id of an item that Reddit
	// will use as an anchor point for the returned listing.
	posts, _, err = reddit.DefaultClient().Subreddit.TopPosts(ctx, "golang", &reddit.ListPostOptions{
		ListOptions: reddit.ListOptions{
			Limit: 100,
			After: resp.After,
		},
		Time: "all",
	})
	if err != nil {
		return
	}

	for _, post := range posts {
		fmt.Println(post.Title)
	}

	return
}
