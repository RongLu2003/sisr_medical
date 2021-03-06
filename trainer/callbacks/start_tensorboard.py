import tensorflow as tf
import subprocess
import atexit

class StartTensorBoard(tf.keras.callbacks.Callback):
    def __init__(self, log_dir):
        super()
        self.log_dir = log_dir
        
    def start_tensorboard(self, log_dir):
        try:
            p = subprocess.Popen(['tensorboard', '--host', '0.0.0.0', '--logdir', self.log_dir])
        except subprocess.CalledProcessError as err:
            print('ERROR:', err)
            
        atexit.register(lambda: p.kill())    
        print('\n\n Starting Tensorboard at: {}\n\n'.format(self.log_dir))
        
    def on_train_begin(self, logs={}):
        self.start_tensorboard(self.log_dir)
