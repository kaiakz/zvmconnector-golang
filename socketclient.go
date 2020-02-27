package zvmconnector

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net"
	"strconv"
	"time"
)

// SDKSocketClient use the sdk api
type SDKSocketClient struct {
	connect net.Conn
}

// NewSDKSocketClient create a SDKSocketClient
func NewSDKSocketClient(addr string, port uint16, timeout time.Duration) (*SDKSocketClient, error) {
	serverAddr := addr + ":" + strconv.Itoa(int(port))
	netType := "tcp4"
	conn, err := net.DialTimeout(netType, serverAddr, timeout)
	if err != nil {
		return nil, nil
	}
	c := &SDKSocketClient{
		connect: conn,
	}
	return c, nil
}

// Fetch the data
func (client *SDKSocketClient) Fetch(api string, apiArgs string) string {
	var buffer bytes.Buffer
	template := "[\"%s\",\"%s\"]"
	str := fmt.Sprintf(template, api, apiArgs)
	_, err := buffer.WriteString(str)
	if err != nil {

	}
	client.connect.Write(buffer.Bytes())

	result, err := ioutil.ReadAll(client.connect)

	buffer.Reset()
	buffer.Write(result)
	return buffer.String()
}

// Close the net.Conn
func (client *SDKSocketClient) Close() {
	client.connect.Close()
}
