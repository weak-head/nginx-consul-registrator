FROM nginx:1.15

# Consul template version
ARG CONSUL_TEMPLATE_VERSION=0.19.5

# Update packages and install curl, runit and unzip
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update -qq && \
    apt-get -y install curl runit unzip && \
    rm -rf /var/lib/apt/lists/*

# Download the specified version of Consul-Template and put it on /usr/local/bin
ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /usr/bin/
RUN unzip /usr/bin/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    mv consul-template /usr/local/bin/consul-template && \
    rm -rf /usr/bin/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip

# Add nginx.service and make it executable
ADD nginx.service /etc/service/nginx/run
RUN chmod a+x /etc/service/nginx/run

# Add consul-template.service and make it executable
ADD consul-template.service /etc/service/consul-template/run
RUN chmod a+x /etc/service/consul-template/run

# Remove the default nginx config
RUN rm -v /etc/nginx/conf.d/*

# Add nginx consul template config
ADD nginx.conf /etc/consul-templates/nginx.conf

# Run nginx and consul-template services
CMD ["/usr/bin/runsvdir", "/etc/service"]