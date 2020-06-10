require 'sinatra/base'
require 'json'


class MyApp < Sinatra::Base
  
  get '/' do
    '<p> hello!</p>'
  end

  post '/api' do
    params = JSON.parse request.body.read
    userid = params["userid"]
    user_json = "{\"user\":{\"age\":29,\"company\":\"White Company\",\"gender\":\"male\",\"id\":\"#{userid}\",\"name\":\"山田太郎\"}}"
    user_hash = JSON.parse(user_json)
    JSON.generate(user_hash)
  end

  run!
end
