myapp Helm chart

To template for dev:

  helm template . --values values.yaml

For staging:

  helm template . --values values-staging.yaml

For production:

  helm template . --values values-production.yaml
