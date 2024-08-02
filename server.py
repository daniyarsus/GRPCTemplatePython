import grpc
from concurrent import futures
import text_processor_pb2
import text_processor_pb2_grpc


class TextProcessorServicer(text_processor_pb2_grpc.TextProcessorServicer):
    def ProcessText(self, request, context):
        response = text_processor_pb2.TextResponse()

        response_from_server = "hi"

        response.processed_text = response_from_server
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    text_processor_pb2_grpc.add_TextProcessorServicer_to_server(TextProcessorServicer(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    print("Server started at port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
