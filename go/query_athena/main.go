package main

import (
	"fmt"
	"log"
	"os"
	"time"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/credentials"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/athena"
)

// query athena

func main() {
	profile := os.Getenv("AWS_DEFAULT_PROFILE")
	region := os.Getenv("AWS_DEFAULT_REGION")
	s3_output_location := os.Getenv("S3_OUTPUT_LOCATION")

	cred := credentials.NewSharedCredentials("", profile)

	// Create a Session with a custom region
	sess := session.Must(session.NewSession(&aws.Config{
		Credentials: cred,
		Region:      aws.String(region),
	}))

	// Create the service's client with the session.
	svc := athena.New(sess)

	var s athena.StartQueryExecutionInput
	s.SetQueryString("SELECT * FROM event_data_test LIMIT 5")

	var q athena.QueryExecutionContext
	q.SetDatabase("event_db_test")
	s.SetQueryExecutionContext(&q)

	var r athena.ResultConfiguration
	r.SetOutputLocation(s3_output_location)
	s.SetResultConfiguration(&r)

	result, err := svc.StartQueryExecution(&s)
	if err != nil {
		log.Println(err)
	}
	fmt.Println(result.GoString())

	var qri athena.GetQueryExecutionInput
	qri.SetQueryExecutionId(*result.QueryExecutionId)

	var qrop *athena.GetQueryExecutionOutput
	duration := time.Duration(2) * time.Second // Pause for 2 seconds

	for {
		qrop, err = svc.GetQueryExecution(&qri)
		if err != nil {
			fmt.Println(err)
			return
		}
		if *qrop.QueryExecution.Status.State != "RUNNING" {
			break
		}
		fmt.Println("waiting.")
		time.Sleep(duration)

	}
	if *qrop.QueryExecution.Status.State == "SUCCEEDED" {

		var ip athena.GetQueryResultsInput
		ip.SetQueryExecutionId(*result.QueryExecutionId)

		op, err := svc.GetQueryResults(&ip)
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Printf("%+v", op)
	} else {
		fmt.Println(*qrop.QueryExecution.Status.State)

	}
}
