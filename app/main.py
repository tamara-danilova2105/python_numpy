from app.features.numpy_basics import feature_basis
from app.features.numpy_indexing import feature_indexing
from app.features.numpy_stats import feature_stats
from app.features.numpy_reshape import feature_reshape
from app.features.numpy_linalg import feature_linalg
from app.features.numpy_io import feature_io

def main():
    feature_basis()
    feature_indexing()
    feature_stats()
    feature_reshape()
    feature_linalg()
    feature_io()

if __name__ == "__main__":
    main()
