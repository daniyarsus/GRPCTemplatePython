import grpc
import text_processor_pb2
import text_processor_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = text_processor_pb2_grpc.TextProcessorStub(channel)
        text = "Hello, how can AI help you today?"
        response = stub.ProcessText(text_processor_pb2.TextRequest(text=text))
        print("Processed Text: ", response.processed_text)


if __name__ == '__main__':
    run()
