from django.shortcuts import render

def index(request):
    """
    Dataset should be bifurcated into 3 subsets, namely:
        Training: Dataset to be used while training
        Validation: Dataset to be tested against while training
        Test: Dataset to be tested against after we trained a model
    """
    return render(request, 'Home/index.html')



