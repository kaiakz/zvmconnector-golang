package zvmconnector

import (
	"net"
	"strconv"
	"time"
)

// RestClient use the sdk api
type RestClient struct {
	connect net.Conn
}

// NewRestClient create a RestClient
func NewRestClient(addr string, port uint16, timeout time.Duration) (*RestClient, error) {
	serverAddr := addr + ":" + strconv.Itoa(int(port))
	netType := "tcp4"
	conn, err := net.DialTimeout(netType, serverAddr, timeout)
	if err != nil {
		return nil, nil
	}
	c := &RestClient{
		connect: conn,
	}
	return c, nil
}

// Fetch the data
func (client *RestClient) Fetch(apiName string, apiArgs []string, apikArgs map[string]interface{}) Response {
	return Response{}
}

// Close the net.Conn
func (client *RestClient) Close() {
	client.connect.Close()
}
