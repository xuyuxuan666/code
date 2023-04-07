import tensorrt as trt
import onnx
import os

# Load the ONNX model
onnx_model_path = "path/to/your/onnx/model"
onnx_model = onnx.load(onnx_model_path)

# Create a TensorRT engine from the ONNX model
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)
EXPLICIT_BATCH = 1 << (int)(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH)
with trt.Builder(TRT_LOGGER) as builder, builder.create_network(EXPLICIT_BATCH) as network, trt.OnnxParser(network, TRT_LOGGER) as parser:
    builder.max_batch_size = 1
    builder.max_workspace_size = 1 << 28 # 256 MiB
    if not os.path.exists(onnx_model_path):
        print('ONNX model not found')
    with open(onnx_model_path, 'rb') as model:
        if not parser.parse(model.read()):
            for error in range(parser.num_errors):
                print(parser.get_error(error))
            return None
    engine = builder.build_cuda_engine(network)

# Save the TensorRT engine to a file
engine_path = "path/to/save/trt/engine"
with open(engine_path, "wb") as f:
    f.write(engine.serialize())
